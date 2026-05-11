# Prompt For Ankos Codex: Batched Rollout Performance Pass

You are working in `/home/jake/Developer/ankos`.

Goal: add a clean batched rollout path to the `ca` package so the PE repo can
generate multiple same-domain episodes with one CA call instead of looping over
`ca.rollout(...)` one episode at a time.

Please inspect the current repo before editing, especially:

- `src/ca/rollout.py`
- `src/ca/specs.py`
- `src/ca/seeds.py`
- `src/ca/loci.py`
- `src/ca/__init__.py`
- `tests/test_rollout.py`
- `tests/test_specs.py`
- `tests/test_seeds.py`

Current state I observed from PE:

- `ca.rollout(dynamics, rule_id, seed_state, steps, return_coords=True)` is
  single-episode only.
- It returns `RawEpisode(domain, shape, rule_id, steps, states, coords,
  metadata)`.
- Unbatched `states` shape is `(T, *spatial_shape)`.
- `coords` shape is `(T * cell_count, 4)` when materialized.
- `Dynamics` is already reusable and excludes per-episode inputs.
- `rollout.py` already vectorizes within one spatial update, but callers still
  pay Python overhead for each episode.
- PE timing on an NVIDIA RTX A6000 for a tiny `configs/multi.py --batch-size 4`
  smoke showed data-side work is meaningful: seed rendering about `0.115s`,
  rollout about `0.036s`, and host collation/device transfer about `0.045s`.

What to build:

- Add a public batched rollout API, probably named something like
  `ca.rollout_batch(...)`, exported from `ca.__init__`.
- Preserve existing `ca.rollout(...)` behavior and tests.
- The batched API should accept one shared `Dynamics`, per-row `rule_ids`,
  per-row `seed_states`, shared `steps`, and `return_coords`.
- It should return a raw NumPy-compatible result, probably a new dataclass in
  `specs.py` rather than forcing batched data into `RawEpisode`.
- Desired state shape is `(B, T, *spatial_shape)`.
- Desired `rule_ids` metadata should preserve each row's rule id.
- Coords can probably be shared as one canonical `(T * cell_count, 4)` array
  because all rows in one batched call should share dynamics, shape, and steps.
  Use your judgement if another representation is cleaner.

Important boundaries:

- Keep this a raw CA library feature. Do not add PE tokenization, masks,
  torch tensors, device policy, dataset split policy, rule-pool policy, or
  checkpoint/training concepts.
- Keep outputs NumPy-compatible.
- Keep RNG policy outside rollout. Batched rollout should consume already
  rendered seed states, not decide streams or sample seeds.
- It is fine to require same `Dynamics`, same shape, and same `steps` per batch.
  PE can group examples by dataset/layout before calling it.
- Do not obscure correctness for clever speed. Start with clear vectorized paths
  for the existing Phase 1 families.

Likely implementation targets:

- AR2 scalar recurrence: vectorize across batch. Seed states likely arrive as
  `(B, 2)` and output should be `(B, T)`.
- Spatial lookup families (`dyadrads_1d`, `dyadaxes_2d`, `dyadaxes_3d`):
  support seed states shaped `(B, *shape)` and output `(B, T, *shape)`.
- Avoid rebuilding coordinate spaces, current coordinate grids, selector
  offsets, and canonical coords once per row when they are shared by the batch.
- If straightforward, factor the single-row implementation so `rollout(...)`
  can delegate to the batched implementation for `B=1`, but only do that if it
  keeps the code simpler.

Tests to add:

- Batched AR2 produces the same rows as looping over `ca.rollout`.
- Batched 1D, 2D, and 3D lookup rollout produce the same rows as looping.
- `return_coords=False` skips coord materialization.
- Shape mismatch errors are clear.
- The public export works as `import ca; ca.rollout_batch(...)`.
- Existing tests still pass.

Verification:

Run:

```bash
uv run pytest -q
```

If you add a tiny benchmark or timing helper, keep it lightweight and optional.
The key acceptance criterion is correctness parity with repeated `rollout`
calls and a public batch result shape that PE can consume directly.

# Feedback

• Yes, but I would adjust PE. ca.rollout_batch(...) is useful only if PE feeds
  it actual same-domain groups. With the current multi-domain round-robin,
  batch_size=4 often means one 0D, one 1D, one 2D, one 3D example, so a same-
  Dynamics rollout batch degenerates into four batches of size 1.

  Best shape:

  PE plans examples
    -> group by dataset/dynamics/shape/steps
    -> batch-render seeds per group
    -> ca.rollout_batch(...) per group
    -> serialize rows or serialize batch
    -> collate mixed model batch

  I would not move stream policy into ANKoS. But I would change PE from
  “realize one example at a time” to “plan a batch, then realize it in
  groups.”

  My Recommendation

  1. Keep training generation streaming/on-demand, not fully pre-generated.
     Pre-generating all training episodes looks tempting, but it pushes the
     bottleneck into disk, storage, stale artifacts, and less flexible eval/
     sampling. The procedural stream design is a strength. Pre-generate only
     fixed eval sets, small smoke fixtures, or optional benchmark caches.
  2. Batch seed generation.
     The prompt’s timing says seed rendering is more expensive than rollout.
     That is a signal. We should add either ca.seeds.render_batch(...) or a PE
     helper that calls CA seed primitives in vectorized form. Since seed
     definitions are CA concepts, I’d prefer the primitive live in ANKoS,
     while PE still chooses the seed recipes and RNGs.
  3. Change PE scheduling so batches are generation-friendly.
     For multi, either:
      - sample one domain per optimizer step, simplest and fastest; or
      - build per-domain sub-batches, call rollout_batch per domain, then
        concatenate for one mixed optimizer step.
  4. Precompute static PE metadata.
     For each layout, coords, position ids, token types, time indices, and
     probably attention masks are mostly fixed. Rebuilding those per episode
     is waste. This may matter as much as rollout batching.

  So yes: the prompt is aligned, but the real win needs a PE-side batch
  planner. ANKoS should expose raw batch kernels; PE should choose rows, RNGs,
  seed recipes, grouping, tokenization, collation, and device movement.


# Seed Count

• It depends on shape and whether exact dedupe is enabled.

  With the current default ca.seeds.structured(shape) settings:

  0D shape ()          -> 2
  1D shape (123,)      -> 492
  2D shape (11, 11)    -> 402
  3D shape (5, 5, 5)   -> 502

  Raw before dedupe:

  (123,)      -> 1848 raw, 492 deduped
  (11, 11)   -> 508 raw, 402 deduped
  (5, 5, 5)  -> 560 raw, 502 deduped

  So for our PE target structured spatial datasets, it is hundreds of seed specs per
  shape, not a tiny fixed catalog.

───────────────────────────────────────────────────────────────────────────────────────


› for all three together deduped?


• For the three spatial PE target shapes together, deduped:

  1D (123,)      492
  2D (11, 11)   402
  3D (5, 5, 5)  502
  Total        1396

  So 1,396 structured seed specs total across those three target branches.


› and with 1396 seeds, and 3 domains and 256 rules per domain, how many total episodes
  is that?


• 1,396 seeds * 3 domains * 256 rules = 1,072,128 episodes.

  So just over 1.07 million episodes.


# Parameter Count

• With depth = 4, the model shape is:

  n_layer = 4
  n_embd = 384
  n_head = 4
  n_kv_head = 4
  head_dim = 96
  sequence_len = 2048

  Parameter count depends slightly on vocab size:

  t0d vocab 103      -> 7,236,360 params
  t1d/t2d/t3d vocab 8 -> 7,090,440 params
  multi vocab 105    -> 7,239,432 params

  So for the full multi-domain model at depth 4: 7.24M parameters.


# Episode Count

  The token-window part aligns:

  t+0D: 2046 loss tokens
  t+1D: 16 * 123 = 1968
  t+2D: 16 * 121 = 1936
  t+3D: 16 * 125 = 2000
  multi round: 2046 + 1968 + 1936 + 2000 = 7950

  But the episode counts are stale relative to current code/model params.

  Current code gives:

  t0d   params 7,236,360 -> 86,836,320 tokens -> 42,442 episodes
  t1d   params 7,090,440 -> 85,085,280 tokens -> 43,235 episodes
  t2d   params 7,090,440 -> 85,085,280 tokens -> 43,950 episodes
  t3d   params 7,090,440 -> 85,085,280 tokens -> 42,543 episodes
  multi params 7,239,432 -> 86,873,184 tokens

  Also important: current code does not actually split the multi budget across the four
  dataset families. It currently prepares each branch with its own full branch budget,
  so exhausting all four multi streams would be about:

  342,096,012 loss tokens
  172,170 episodes total

  If we want the multi config to split its 86,873,184 target tokens across the four
  domains, then the rough split should be:

  t0d: 10,616 episodes
  t1d: 11,036 episodes
  t2d: 11,219 episodes
  t3d: 10,860 episodes

  Or as mixed four-domain rounds:

  86,873,184 / 7,950 = 10,928 mixed rounds
  = 43,712 individual episodes

  So your table is conceptually right on the window math, but not aligned with the
  current implementation for target episode counts or multi-budget splitting.
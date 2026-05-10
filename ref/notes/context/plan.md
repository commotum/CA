# Refactor Plan

This is the staged plan for the CA extraction and PE repair. The source of
truth for final layout and naming is `context/REFACTOR_TARGET.md`.

## Reference Documents

- `context/REFACTOR_TARGET.md`: final repo layout and naming rules
- `context/handoff_contract.md`: tight `ankos`/`pe` runtime boundary
- `context/REFACTOR_CA.md`: CA extraction guide
- `context/REFACTOR_PE.md`: PE target layout guide
- `context/experiment_architecture.md`: explicit-coordinate PE architecture
- `context/pe-atlas.md`: pre-refactor code atlas and old-to-new path map
- `/home/jake/Developer/ankos/ref/notes/rollout.md`: rollout intent
- `/home/jake/Developer/ankos/ref/notes/numpy-target.md`: NumPy public API target

## Phase 0: Guardrails

Goal: make sure every later edit follows the same authority chain.

Steps:

- Treat `context/REFACTOR_TARGET.md` as the naming/layout source of truth.
- Use `old/data/components` as the CA catalog source path.
- Keep `ankos` public CA rollout NumPy-compatible.
- Keep torch conversion at `pe/components/batch.py`.
- Keep vectorization/speed work and custom mask work out of the first repair pass.

Exit criteria:

- The active docs agree on target paths, handoff shape, and NumPy-vs-torch boundary.

## Phase 1: Move CA Sources

Goal: establish the `ankos/src/ca` target modules with minimal behavioral
change.

Steps:

- Move old CA catalogs:

```text
old/data/components/loci.py          -> /home/jake/Developer/ankos/src/ca/loci.py
old/data/components/alphabets.py     -> /home/jake/Developer/ankos/src/ca/alphabets.py
old/data/components/neighborhoods.py -> /home/jake/Developer/ankos/src/ca/neighborhoods.py
old/data/components/frontiers.py     -> /home/jake/Developer/ankos/src/ca/frontiers.py
old/data/components/seeds.py         -> /home/jake/Developer/ankos/src/ca/seeds.py
old/data/components/rules.py         -> /home/jake/Developer/ankos/src/ca/rules.py
old/data/generate.py                 -> /home/jake/Developer/ankos/src/ca/rollout.py
```

- Add/normalize:

```text
/home/jake/Developer/ankos/src/ca/specs.py
/home/jake/Developer/ankos/src/ca/boundary.py
/home/jake/Developer/ankos/src/ca/rng.py
/home/jake/Developer/ankos/src/ca/__init__.py
/home/jake/Developer/ankos/src/ca/py.typed
```

Exit criteria:

- Files exist in the target tree.
- Imports are local to `ca` where possible.
- No PE tokenization, masks, split policy, PE cache, or model code enters `ankos`.

## Phase 2: Rewire CA Internals

Goal: make `ankos` coherent as a standalone CA package.

Steps:

- Convert old repo-local imports to `ca` internal imports.
- Centralize boundary reads in `ca.boundary`.
- Make Phase 1 rule instantiation executable for supported families.
- Make frontier behavior explicit: support `full_next_slice`, reject the rest.
- Keep future stubs visible but honest with `NotImplementedError`.
- Add focused tests under `/home/jake/Developer/ankos/tests`.

Exit criteria:

- `ca.rollout()` works for Phase 1 AR2, 1D, 2D, and 3D examples.
- Unsupported frontiers fail loudly.
- Basic `ankos` tests pass.

## Phase 3: Target NumPy In CA

Goal: make the `ankos` public API NumPy-compatible before PE depends on it.

Steps:

- Return `RawEpisode.states` as ndarray-like arrays.
- Return materialized `coords` as integer ndarray-like arrays when requested.
- Make seed rendering produce ndarray-like raw states.
- Replace public torch RNG helpers with NumPy RNG helpers.
- Keep any future torch backend optional and out of the baseline contract.

Exit criteria:

- Public `ca` rollout has NumPy semantics.
- No public `ankos` API requires torch tensors or device placement.
- Shapes match `context/handoff_contract.md`.

## Phase 4: CA Polish

Goal: finish the standalone package enough for PE to consume it safely.

Steps:

- Tighten JSON-safe specs and metadata.
- Normalize domain strings as `t+0d`, `t+1d`, `t+2d`, `t+3d`.
- Export only the supported Phase 1 surface from `ca.__init__`.
- Update `ankos` README/package metadata only as needed.

Exit criteria:

- `ankos` can be imported as `ca`.
- `ca.rollout()` and `ca.rng` match the handoff contract.

## Phase 5: Repair PE Target Tree

Goal: reshape PE around the normalized target layout after CA extraction.

Steps:

- Create/repair config files:

```text
configs/t0d.py
configs/t1d.py
configs/t2d.py
configs/t3d.py
configs/multi.py
```

- Create/repair dataset branches:

```text
data/0d-ar2-97/
data/1d-dyadrads/
data/2d-dyadaxes/
data/3d-dyadaxes/
data/datasets.py
```

- Move PE common-core code into:

```text
components/tokenizer.py
components/batch.py
components/posenc.py
components/attention.py
components/optimizer.py
components/evals.py
components/checkpoint.py
```

Exit criteria:

- PE imports resolve against target paths.
- Dataset branches expose the target `manifest/` files and `prepare.py`.
- Legacy text/parquet/BPE paths are not in the active next-state flow.

## Phase 6: Wire The Handoff

Goal: make PE consume `ankos` through the documented contract.

Steps:

- Build `ca.Dynamics` values from dataset manifests/preparation scripts.
- Derive episode RNGs and rule ids from PE stream policy.
- Render seed states through `ca`.
- Call `ca.rollout()` from `components/batch.py`.
- Serialize `ca.RawEpisode` in `components/tokenizer.py`.
- Convert NumPy-compatible arrays with `torch.from_numpy(...)` at the batch boundary.
- Collate token ids, targets, loss masks, coords, position ids, and layout ids.
- Build the dense state-causal mask.

Exit criteria:

- One train batch can be built for each single-domain dataset.
- One mixed batch can be built for `multi`.
- Handoff fields match `context/handoff_contract.md`.

## Phase 7: Restore Model, Train, Eval

Goal: get the PE training/evaluation loop working on the repaired structure.

Steps:

- Make `model.py` consume componentized attention and PE cache application.
- Make `components/posenc.py` the explicit-coordinate PE cache path.
- Make `train.py` load configs, datasets, tokenizer, batches, model, optimizer, evaluator, and checkpoints.
- Make `eval.py` load exported or run checkpoints and rebuild needed components.
- Keep exported checkpoints separate from resumable `run_dir/checkpoints`.

Exit criteria:

- A smoke train loop runs far enough to build batches, forward, loss, backward, and checkpoint.
- A smoke eval can load a checkpoint and run next-state metrics.

## Phase 8: Clean And Tidy

Goal: remove migration drag after the system works.

Steps:

- Remove stale imports and dead compatibility shims from active paths.
- Check docs against actual paths.
- Normalize `readme.md` files for datasets and checkpoints.
- Run focused tests for `ankos` and PE.
- Confirm no target tree naming drift.

Exit criteria:

- Target tree matches `context/REFACTOR_TARGET.md`.
- Docs match the implemented handoff and checkpoint layouts.

## Phase 9: Performance Pass

Goal: improve speed after correctness and structure are stable.

Steps:

- Vectorize obvious CA rollout hot paths where it does not obscure correctness.
- Improve PE batch buffering and CPU-to-device transfer.
- Avoid repeated allocation in tokenizer/batch collation.
- Add simple timing checks around rollout, serialization, and batch construction.

Exit criteria:

- Performance changes preserve existing outputs.
- Any backend expansion stays optional and does not replace the NumPy public contract.

## Phase 10: Custom Mask Plan

Goal: plan the custom attention mask module only after the refactor is stable.

Steps:

- Review the dense state-causal mask behavior.
- Identify the target attention backend shape.
- Write a separate mask implementation plan.
- Only then implement the custom mask module.

Exit criteria:

- The mask plan is based on working PE batches, working PE caches, and known bottlenecks.

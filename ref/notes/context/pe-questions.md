# PE Cleanup Questions

These are clarification questions that materially affect cleanup/refactor choices. Files with no useful open questions are omitted.

## `data/batch.py`

- Should the legacy parquet `make_dataloader` compatibility layer remain in `data/batch.py`, move elsewhere, or be deleted?
- Should the current public split name be standardized on `eval` or `val`?
- Is `raw_states_per_episode` intended to mean number of generated states or number of rollout steps/transitions?

## `data/components/alphabets.py`

- Should future-facing stubs remain public in this file, or should unsupported families be removed/hidden until implemented?
- Should `params` be made immutable to match `frozen=True` expectations?
- Should factories accept an optional `name`, since the dataclasses expose that field?

## `data/components/datasets.py`

- Should `DatasetSpec` grow explicit fields for horizon, split/eval conventions, and artifact naming, or should the module docstring/schema be narrowed to current behavior?
- Should dataset factories be collected into a registry keyed by `DatasetSpec.id`, or is discovery by direct function import intentional?

## `data/components/evals.py`

- Should `held_out_rule` use `seed_stream="train"` to isolate rule holdout, or is rule-plus-eval-seed holdout intentional?
- Should `invariance` be over train examples as coded, or held-out examples as documented?
- Is the “Phase 2 Helpers” section still meaningful, or should it be renamed to generic config helpers?

## `data/components/frontiers.py`

- Should every nontrivial frontier factory accept `shape`, matching `time_slice()`, or should `Frontier` remain a deferred spec materialized elsewhere?
- Is `t=0` meant to represent “current relative time” universally, or should time-dependent frontiers carry symbolic/runtime time?

## `data/components/loci.py`

- Should `CoordinateSpace` become the required source of truth for `gather`, instead of inferring `(time, *spatial)` from `values.shape`?
- Should this file keep design-spec prose in docstrings, or should docstrings describe current executable behavior only?
- Is `frame/read_mode` intentionally metadata for external layers, or should `select` enforce/use them?

## `data/components/neighborhoods.py`

- Should explicit support-algebra helpers such as union/intersection/difference be added for merged read loci?
- Should “shell” APIs reject `radius=0` and center-including counts, or is center-as-radius-zero intended?
- Are Phase 2/3 stubs public planned API that should remain importable, or should unfinished names be hidden until implemented?

## `data/components/rules.py`

- Should `Rule` remain a spec object that may or may not have `fn`, or should `instantiate()` always return an executable rule?
- Are Phase 2/3 placeholders intentional public API reservations, or should the refactor either implement them as real aliases/factories or remove them until needed?

## `data/components/seeds.py`

- Should seed specs be serializable catalog data, or is storing callables/selectors inside `Seed.params` acceptable?
- Should all structured seed factories be strictly `t=0`, or should `path()` / `finite_segment()` honor temporal coordinates the way `point()` does?
- Should `dedupe()` mean duplicate rendered tensors, or duplicate support masks independent of selected/fill values?

## `data/generate.py`

- Should `frontier` become real behavior in this file, or should it be removed from the generation contract until implemented?
- Should lookup channels be explicitly binary-only, or should naming/docs support multi-valued channel states intentionally?

## `data/tokenize.py`

- Should the autoresearch BPE compatibility layer remain in `data/tokenize.py`, or should it be split into a separate text-tokenizer module?
- Are position layouts intended to be persisted as JSON/cache artifacts, or are tensor/tuple-key in-memory structures acceptable?
- Should coordinate transforms be strictly spatial, and should full transform params participate in layout identity instead of only `id`?

## `model.py`

- Should `window_pattern` semantics be guaranteed across all attention backends, including SDPA fallback?
- Is `init_weights()` intentionally external, or should model construction always produce train-ready initialization?

## `pe.py`

- Should legacy APIs remain supported, or should `build_cache_bundle()` / `apply_cached_position_encoding()` become the only model-facing path?
- Is the MonSTER key transform intentionally just `time_sign=-1`, or should it be documented as an inverse/symmetric transform?
- Are layout `positions` guaranteed integer `[N,4]`, or should fractional coordinates be preserved and validated explicitly?

## `prepare.py`

- Should `special_tokens_per_episode` remain configurable, or should it be fixed to exactly match `["<bos>", "<domain>"]`?
- Should `dataset_catalog_digest` become a true full-spec digest, or is the current summary digest intentional?

## `train.py`

- Should `train.py` be a smoke-test/runtime validation CLI, or should it become a full training entrypoint with checkpoint save/resume?
- Are original and transformed invariance examples guaranteed to have identical loss-token counts?
- Should future artifacts standardize on `kind` and drop the fallback to `eval`, or is backward compatibility still required?

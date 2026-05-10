# PE Code Micro-Atlas

This atlas describes the pre-refactor Python code, not the older project notes.
The paths below are old paths. The target destinations are governed by
`context/REFACTOR_TARGET.md`.
Section headings keep the old module names; when copying from disk during the
migration, use the corresponding `old/...` source paths in the path map.

## Executive Synthesis

### Pre-Refactor Repo Mental Model

The pre-refactor repo is a procedural next-state transformer experiment stack. It has:

- declarative component catalogs under `data/components/`
- a pure-ish rollout layer in `data/generate.py`
- a runtime realization, tokenization, batching, and mask path across `data/batch.py` and `data/tokenize.py`
- a manifest freezer in `prepare.py`
- positional-encoding cache math in `pe.py`
- a GPT-style model plus optimizer in `model.py`
- a training/eval CLI in `train.py`

The old intended path is manifest-driven: `prepare.py` writes source recipes and stream specs, `train.py` loads those artifacts, `data.batch` realizes examples at runtime, `data.generate` rolls raw states, `data.tokenize` serializes them into model tensors and layout ids, `pe.py` builds cache bundles, and `model.py` trains/evaluates with those caches.

### Old Dependency/Dataflow Sketch

```text
data.components.loci
  -> neighborhoods/frontiers/seeds

alphabets + neighborhoods + frontiers + rules + seeds
  -> datasets

datasets + evals + tokenize.vocab
  -> prepare.py
  -> data/datasets/<run_id>/*.json

prepared artifacts + datasets
  -> train.py
  -> data.batch stream iterators
  -> seeds.render
  -> data.generate.generate_episode
  -> data.tokenize.serialize_episode
  -> data.batch.make_next_state_batch

data.tokenize.position_layouts_from_streams
  -> pe.build_cache_bundle
  -> model.GPT.set_pe_cache
  -> model.GPT.forward
```

### Refactor Path Map

```text
old/data/components/loci.py          -> ankos/src/ca/loci.py
old/data/components/alphabets.py     -> ankos/src/ca/alphabets.py
old/data/components/neighborhoods.py -> ankos/src/ca/neighborhoods.py
old/data/components/frontiers.py     -> ankos/src/ca/frontiers.py
old/data/components/seeds.py         -> ankos/src/ca/seeds.py
old/data/components/rules.py         -> ankos/src/ca/rules.py

old/data/generate.py                 -> ankos/src/ca/rollout.py
old/data/batch.py RNG helpers        -> ankos/src/ca/rng.py

old/data/components/datasets.py      -> pe/data/datasets.py
                                      -> pe/data/<dataset>/prepare.py
old/data/components/evals.py         -> pe/components/evals.py

old/data/tokenize.py                 -> pe/components/tokenizer.py
old/data/batch.py                    -> pe/components/batch.py
old/pe.py                            -> pe/components/posenc.py
old/model.py attention pieces        -> pe/components/attention.py
old/model.py optimizer pieces        -> pe/components/optimizer.py
old/model.py GPT composition         -> pe/model.py
old/prepare.py                       -> pe/data/datasets.py
                                      -> pe/data/<dataset>/prepare.py
old/train.py                         -> pe/train.py
                                      -> pe/eval.py
```

Detailed lookup for normalized CA modules:

```text
ankos/src/ca/specs.py
  old/data/components/datasets.py     DatasetSpec
  old/data/generate.py                Episode / RawEpisode shape
  old/data/components/alphabets.py    Alphabet
  old/data/components/loci.py         CoordinateSpace, Selector, Selection
  old/data/components/neighborhoods.py Neighborhood
  old/data/components/frontiers.py    Frontier
  old/data/components/seeds.py        Seed
  old/data/components/rules.py        RuleChannel, Rule

ankos/src/ca/boundary.py
  old/data/components/loci.py         _BOUNDARY_POLICIES and gather policy logic
  old/data/components/loci.py         native_indices helper dependency stays in loci
  old/data/generate.py                apply_boundary_read
  old/data/generate.py                _read_component boundary setup
  old/data/generate.py                Episode boundary metadata

ankos/src/ca/rng.py
  old/data/batch.py                   splitmix64
  old/data/batch.py                   derive_episode_rng
  old/data/batch.py                   render_seed_state generator call site as NumPy replacement guide
```

Boundary policy lookup that stays PE-side:

```text
old/data/components/datasets.py       default boundaries: AR2 {}, spatial fixed-zero
old/data/components/evals.py          ood_boundary variants
old/prepare.py                        manifest and stream boundary propagation
old/data/batch.py                     eval-row variant boundary overrides
```

### Biggest Mismatches With Old Intent / Docs

- Several files still have docstrings saying they are tentative specs, but they now contain real executable behavior.
- Several modules mix current next-state code with legacy/autoresearch text-tokenizer or parquet dataloader compatibility.
- Component objects are often shallow-frozen dataclasses carrying mutable dicts.
- The spec/executable boundary is blurry: some objects are pure metadata, some are executable, and some promise executable behavior only partially.
- The generator accepts a frontier but ignores it; current rollout is full synchronous spatial update.
- Token and eval stream schemas contain compatibility drift: `eval` vs `kind`, `eval` vs `val`, shifted model-facing time vs raw state time.
- PE cache bundles are the current model path, but `pe.py` still exposes legacy uncached/sequential helpers.

### Highest-Risk Cleanup Areas

- `data/batch.py` and `data/tokenize.py` both carry legacy text/parquet paths alongside next-state experiment code.
- `model.py` attention semantics differ by backend: sliding-window behavior appears FA3-only, while SDPA/masked paths rely on the supplied mask.
- `pe.py` monster factors are not cast like RoPE/axial factors, creating dtype/device risk.
- `data.generate.py` nominally accepts frontiers but does not implement frontier behavior.
- Position layout identity currently relies heavily on transform ids; two transforms with the same id but different params can collide.
- Seed and component catalogs can silently accept invalid or unsupported inputs and produce empty/stale behavior.

### Likely Refactor Boundaries

- Move CA catalogs from `old/data/components/*` into `ankos/src/ca/*`.
- Move old raw rollout from `old/data/generate.py` into `ankos/src/ca/rollout.py` and enforce frontier semantics there.
- Split legacy text/tokenizer/dataloader compatibility away from the next-state paths in `components/batch.py` and `components/tokenizer.py`.
- Make `components/posenc.py` the explicit-coordinate PE cache path.
- Split `old/prepare.py` into shared PE dataset helpers in `data/datasets.py` and dataset-local `data/<dataset>/prepare.py` scripts.
- Keep training orchestration in `train.py`; standalone checkpoint evaluation belongs in `eval.py`.

## `data/batch.py`

Target path: `pe/components/batch.py` for runtime batching; RNG helpers move to
`ankos/src/ca/rng.py`.

Role: runtime next-state example realization and batching, plus legacy autoresearch parquet text dataloader compatibility.

Important dependencies:

- `torch`
- `data.generate.generate_episode`
- `data.tokenize`
- `data.components.seeds.render`
- legacy lazy/runtime dependencies on `prepare`, `os`, and `pyarrow.parquet`

Top-level surface:

- constant: `ATTENTION_POLICY_STATE_CAUSAL_DENSE`
- dataclasses: `RuntimeExample`, `InvariancePair`
- deterministic stream helpers: `splitmix64`, `derive_episode_rng`, `derive_rule_id`, `derive_variant`
- stream realization: `stream_train_examples`, `iter_eval_streams`, `iter_invariance_pairs`
- seed helpers: `render_seed_state`, `derive_seed_spec`
- batch/mask builders: `build_state_causal_attention_mask`, `build_batch_attention_masks`, `build_batch_loss_masks`, `make_next_state_batch`
- legacy text path: `_document_batches`, `make_dataloader`

Function notes:

- `RuntimeExample` stores one accepted generated and serialized episode with ids, split, rule, rng, and metadata.
- `InvariancePair` stores original/transformed serialized examples for coordinate-transform eval.
- `splitmix64` and `derive_episode_rng` make deterministic per-episode seeds from stream namespaces.
- `derive_rule_id` cycles rule ids; only `cycle` policy is supported.
- `derive_variant` cycles variant specs and returns `{}` when no variants exist.
- `eval_row_from_stream` expands compact eval streams into deterministic row descriptors.
- `stream_train_examples` derives rule/seed/variant, renders a seed, generates an episode, tokenizes it, filters it, and yields `RuntimeExample`.
- `iter_eval_streams` does fixed eval realization from eval stream specs and source manifests.
- `iter_invariance_pairs` emits paired original/transformed serialized examples when a transform is present.
- `runtime_filter_accepts` accepts empty filters and raises for non-empty filters, so rollout filtering is not actually implemented.
- `build_state_causal_attention_mask` creates dense `[T,T]` state-causal masks; BOS/domain are visible, state tokens see states up to their source time.
- `build_batch_attention_masks` pads token metadata and stacks dense masks.
- `build_batch_loss_masks` pads ids, targets, loss masks, coords, position ids, layout ids, and lengths.
- `make_next_state_batch` merges tensors/metadata and moves tensor fields to device, defaulting to CUDA.
- `_document_batches` and `make_dataloader` implement the old parquet text next-token path.

Notable mismatches:

- Two unrelated batching paths live in one file: next-state episode batching and legacy text dataloading.
- Runtime filters are advertised but non-empty filters are unimplemented.
- Padding query rows are not fully masked when `valid_token` exists; invalid keys are masked.
- Split naming drifts between `eval` and legacy `val`.
- `raw_states_per_episode` is passed as `steps`, which may be confusing.

## `data/components/alphabets.py`

Target path: `ankos/src/ca/alphabets.py`.

Role: finite raw value-space catalog for dataset values before tokenization, with some future value-space stubs.

Important dependencies: standard library only: `math`, `dataclass`, `Mapping`, `Sequence`, `Any`, `Hashable`, `Literal`.

Top-level surface:

- aliases: `Value`, `ValueSpace`
- dataclasses: `Alphabet`, `IntegerSpace`, `RealInterval`
- factories: `int_range_alphabet`, `float_range_alphabet`, `boolean`, `symbolic`
- stubs: `composite`, `integer_space`, `real_interval`

Function notes:

- `Alphabet` stores finite values, family, params, and optional name.
- `IntegerSpace` and `RealInterval` are constructible dataclasses but their factories are unimplemented.
- `int_range_alphabet` validates positive integer size and returns contiguous integer values.
- `float_range_alphabet` validates finite numeric start/step and returns evenly spaced float values.
- `boolean` returns integer values `(0, 1)`.
- `symbolic` accepts non-empty unique `int` or `str` values, rejecting bools and floats.
- `composite`, `integer_space`, and `real_interval` always raise.

Notable mismatches:

- Docstrings say tentative/catalog-only, but finite factories are implemented.
- Frozen dataclasses carry mutable dict params.
- `symbolic` type hints allow `Hashable`, while runtime allows only `int | str`.
- `Value` includes floats, but symbolic alphabets reject floats.
- `name` fields exist but factories do not accept names.

## `data/components/datasets.py`

Target path: useful PE dataset policy moves to `pe/data/datasets.py` and
dataset-specific facts move to `pe/data/<dataset>/prepare.py`.

Role: dataset catalog. It composes alphabets, neighborhoods, frontiers, rules, and seeds into complete `DatasetSpec` objects.

Important dependencies:

- `dataclass`, `Mapping`, `Sequence`
- `data.components.alphabets`
- `data.components.neighborhoods`
- `data.components.frontiers`
- `data.components.rules`
- `data.components.seeds`

Top-level surface:

- dataclass: `DatasetSpec`
- helper: `_spatial_seeds`
- factories: `ar2_0d_97`, `dyadrads_1d`, `dyadaxes_2d`, `dyadaxes_3d`

Function notes:

- `DatasetSpec` stores id, domain, shape, alphabet, neighborhoods, frontier, rule, seeds, boundary, and params.
- `_spatial_seeds` returns a Bernoulli seed plus structured seeds for a spatial shape.
- `ar2_0d_97` defines scalar `t+0d`, shape `()`, integer alphabet size 97, AR2 neighborhood/rule, pair seed, and no boundary.
- `dyadrads_1d` defines `1d-dyadrads`, shape `(123,)`, boolean alphabet, dyadrads neighborhood/rule, spatial seeds, fixed-zero boundary.
- `dyadaxes_2d` defines `2d-dyadaxes`, shape `(11, 11)`, boolean alphabet, dyadaxes neighborhood/rule, spatial seeds, fixed-zero boundary.
- `dyadaxes_3d` defines `3d-dyadaxes`, shape `(5, 5, 5)`, boolean alphabet, dyadaxes neighborhood/rule, spatial seeds, fixed-zero boundary.

Notable mismatches:

- Docstring still says tentative and mentions default horizon/split/artifact metadata that `DatasetSpec` does not explicitly carry.
- Dataset specs hold component objects directly, not serializable recipes.
- Domain notation drifts between docs like `t+0D` and code values like `t+0d`.
- There is no registry keyed by dataset id in this file.

## `data/components/evals.py`

Target path: reusable evaluation routines move to `pe/components/evals.py`;
stream-construction policy belongs in `pe/data/datasets.py` when shared by
dataset preparation.

Role: declarative eval protocol catalog. It produces immutable `EvalSpec` records for manifest preparation.

Important dependencies: standard library `dataclass`, `Callable`, `Mapping`, `Sequence`, `Any`, `Literal`.

Top-level surface:

- alias: `EvalKind`
- constants: OOD-scale shapes/token overrides, source-state count, context multiplier, default invariance transforms
- dataclass: `EvalSpec`
- factories: `held_out_rule`, `held_out_seed`, `ood_horizon`, `ood_scale`, `ood_boundary`, `invariance`
- helper/registry: `from_config`, `EVAL_FACTORIES`

Function notes:

- `EvalSpec` stores id, kind, and params.
- `_base_params` normalizes common rule/seed pool and variant fields.
- `held_out_rule` selects eval rule pool and default eval seed stream.
- `held_out_seed` selects train rules with eval seed stream.
- `ood_horizon` adds max-token multiplier and fill-token-window policy.
- `ood_scale` adds per-dataset larger shapes and optional max-token overrides.
- `ood_boundary` returns fixed-one, periodic, and reflective boundary variants.
- `invariance` builds transform-variant eval over train rule/seed streams.
- `from_config` converts strings, mappings, or existing specs into `EvalSpec`s.

Notable mismatches:

- `held_out_rule` docstring says rule holdout, but implementation also uses eval seeds.
- `invariance` docstring says held-out examples, but implementation uses train rules and train seeds.
- `kind` and `id` currently duplicate each other.
- Section comment says Phase 2 helpers, while the file otherwise describes Phase 1 evals.

## `data/components/frontiers.py`

Target path: `ankos/src/ca/frontiers.py`.

Role: frontier/update-site selector catalog. Current executable behavior is mostly a single full-time-slice frontier; most APIs are placeholders.

Important dependencies:

- `dataclass`, `Mapping`, `Sequence`, `Any`, `Literal`
- `data.components.loci`

Top-level surface:

- aliases: `CombineMode`, `Metric`, `Region`
- dataclass: `Frontier`
- implemented: `time_slice`
- stubs: `where`, `schedule_class`, `spatial_subspace`, `diagonal`, `parity_sublattice`, `metric_region`, `ring_growth`, `active_wavefront`, `compose`, `skipped_slices`, `row`, `plane`, `moving_subspace`

Function notes:

- `Frontier` stores selector components, combine mode, name, and params.
- `time_slice(shape)` builds a selector over the absolute current slice using `loci.coordinate_space`, `absolute_universe(..., t=0)`, and lex order.
- All other public factories currently raise.

Notable mismatches:

- `time_slice` hard-codes `t=0`, so “current time” is represented as relative zero rather than runtime time.
- Most factory signatures lack shape even though a universe needs shape.
- Several docstrings mention helper predicates not currently used.
- `compose` is documented but unimplemented.

## `data/components/loci.py`

Target path: `ankos/src/ca/loci.py`.

Role: tensor DSL for canonical `[t, x, y, z]` coordinate spaces, universes, predicates, selection masks, ordering, and boundary-aware gather.

Important dependencies: `torch`, `dataclass`, `Callable`, `Mapping`, `Sequence`, `Any`, `Literal`.

Top-level surface:

- aliases/constants: canonical axes, spatial axes, axis columns, boundary policies
- dataclasses: `CoordinateSpace`, `Selector`, `Selection`
- coordinate helpers: `coordinate_space`, `active_axes`, `axis_values`, `coord_vectors`, `coord_grid`
- universe/selector helpers: `absolute_universe`, `offset_universe`, `selector`, `select`, `mask`
- mask/order/projection helpers: `combine_masks`, `not_mask`, `order_lex`, `axis_project`
- predicates/reductions: `predicate`, `coord_eq`, `coord_between`, `sum_axes`, `count_where`, `norm`, `mod_eq`, `state_exists`
- tensor access: `gather`, `native_indices`

Function notes:

- `CoordinateSpace` describes canonical intervals for a spatial shape and optional time extent.
- `Selector` stores universe, predicates, combine/order/frame/read-mode metadata.
- `Selection` stores selected coords, support mask, and original universe.
- `coordinate_space` validates rank `0..3`, positive dimensions, optional positive steps, and centered intervals.
- `absolute_universe` returns flattened absolute coordinates, optionally restricted to time/axes.
- `offset_universe` returns flattened relative offsets over time offsets and spatial ranges.
- `select` evaluates selectors and orders selected coordinates.
- `combine_masks`, `not_mask`, and predicate helpers implement Boolean/coordinate logic.
- `gather` maps canonical coords into native tensor indices and applies boundary handling.
- `native_indices` converts canonical coords to index tensors for a given `CoordinateSpace`.

Notable mismatches:

- `frame` and `read_mode` are stored but not enforced by `select`.
- `coord_grid(frame="relative")` validates frame but does not change output.
- `order_lex` returns coordinates, not indices, despite docstring wording.
- `CoordinateSpace.intervals` is trusted when user-supplied.
- Boundary handling is asymmetric around time vs spatial axes.
- Rank-0 no-time `coord_grid` returns shape `(4,)`, which may surprise consumers expecting `(1, 4)`.

## `data/components/neighborhoods.py`

Target path: `ankos/src/ca/neighborhoods.py`.

Role: neighborhood factory catalog over `loci`, producing source-relative read selectors for CA-style rules.

Important dependencies:

- `dataclass`, `Mapping`, `Sequence`, `Any`, `Literal`
- `data.components.loci`

Top-level surface:

- aliases: `CombineMode`, `Metric`, `Region`
- dataclass: `Neighborhood`
- implemented factories: `self_at`, `axis_shell`, `l1_shell`, `change_count_shell`, `ar2_0d`, `dyadrads_1d`, `dyadaxes_2d`, `dyadaxes_3d`, `compose`
- stubs: `literal_offsets`, `history`, `radius`, `shell`, `directional_line`, `directional_fov`, `moore`, `von_neumann`

Function notes:

- `Neighborhood` stores selector components, combine mode, name, and params.
- `self_at` selects a single temporal offset with spatial offsets zero.
- `axis_shell` selects two signed offsets along one axis at exact positive radius.
- `l1_shell` selects exact L1-distance offsets over axes, allowing radius zero.
- `change_count_shell` selects offsets whose count of nonzero axes is in a count set.
- `ar2_0d` composes self reads at default offsets `(0, -1)`, but accepts arbitrary offsets.
- `dyadrads_1d` composes self, radius-1 x-shell, and radius-2 x-shell.
- `dyadaxes_2d` composes self, cardinal L1 shell, and diagonal change-count shell.
- `dyadaxes_3d` composes self, face L1 shell, and edge/corner change-count shell.
- `compose` flattens component tuples and records combine metadata.

Notable mismatches:

- `combine="merge"` is only metadata; no selector merging/deduplication occurs.
- Composing compound neighborhoods loses one nesting level.
- Some “shell” APIs allow center/radius-zero behavior.
- Spatial factories accept arbitrary time offsets, including future-positive values.
- Many Phase 2/3 names are importable but unimplemented.

## `data/components/rules.py`

Target path: `ankos/src/ca/rules.py`.

Role: rule catalog/spec layer for CA-style updates. It defines rule/channel descriptors and named Phase 1 rule families.

Important dependencies: standard library `Callable`, `Mapping`, `Sequence`, `dataclass`, `Any`, `Literal`.

Top-level surface:

- aliases: `UpdateFn`, `Aggregate`, `DecodeMode`, `GateType`
- dataclasses: `RuleChannel`, `Rule`
- implemented: `instantiate`, `validate`, `exhaustive`, `totalistic`, `gate`, `lookup`, `compose`, `formulaic`, `ar2_modular_0d`, `dyadrads_1d`, `dyadaxes_2d`, `dyadaxes_3d`
- stubs: `isotropic`, `histographic`, `stochastic`, gate aliases, `binary_lookup`, `modular_ar`, `dyadaxes`

Function notes:

- `RuleChannel` describes one component channel and its pipeline.
- `Rule` describes a rule family or instantiated rule, with optional executable `fn`.
- `instantiate` sets `rule_id`, validates against metadata `R`, and creates an executable callable only for `ar2_modular_0d`.
- `validate` computes lookup state count and rule count; it does not validate inputs.
- `exhaustive` creates ordered-pattern channels.
- `totalistic` creates aggregate channels.
- `gate` wraps a channel/pipeline and forces binary `state_count=2`.
- `lookup` creates an LSB-rule-bits lookup rule and computes metadata if channel state counts exist.
- `compose` attaches channels to an output rule.
- `formulaic` wraps a callable/params in a generic rule.
- `ar2_modular_0d` defines the second-order modular recurrence family.
- `dyadrads_1d`, `dyadaxes_2d`, and `dyadaxes_3d` define current spatial lookup families with `R=256`.

Notable mismatches:

- `instantiate` promises concrete callable behavior but only constructs one for AR2.
- Non-AR2 instantiated rules often still have `fn=None`.
- `validate` is named like a checker but only computes counts.
- Gate names imply non-binary transforms, but gate metadata always sets binary state count.
- Phase 3 “aliases” are placeholders rather than aliases.

## `data/components/seeds.py`

Target path: `ankos/src/ca/seeds.py`.

Role: seed catalog plus concrete seed renderer for initial states.

Important dependencies:

- `torch`
- `data.components.loci`
- `itertools`, `math`, `dataclass`, `Mapping`, `Sequence`, `Literal`, `Any`

Top-level surface:

- aliases: `Metric`, `Stratum`, `DedupeMode`
- dataclass: `Seed`
- core factories: `pair`, `uniform_pair`, `bernoulli`, `selector_seed`, `point`
- structured factories: `subspace`, `finite_segment`, `body`, `compound`, `region`, `periodic`, `fractal`, `spiral`, `path`, `transform`
- runtime helpers: `render`, `dedupe`, `structured`, `constant`

Function notes:

- `Seed` stores support selector, selected/fill values, distribution, family, params, and name.
- `pair` returns a fixed scalar two-history seed.
- `uniform_pair` samples scalar pair values at render time.
- `bernoulli` defines stochastic binary initial-state support; unsupported support forms can become `None`.
- `selector_seed` fills selected coords with selected value.
- `point`, `subspace`, `finite_segment`, `body`, `compound`, `region`, and `periodic` build selector-backed structured seeds.
- `fractal` and `spiral` wrap callable predicates into seed params.
- `path` selects explicit listed points, optionally thickened; it does not interpolate.
- `transform` currently supports inversion; reflect/permute/rotate are stubs.
- `render` materializes a `Seed` into a `torch.long` tensor.
- `dedupe` removes duplicate rendered tensors.
- `structured` enumerates many structured seed families and optionally dedupes.
- `constant` creates full-shape constant seeds.

Notable mismatches:

- This is runtime rendering code, not just catalog specs.
- `symmetry` dedupe mode exists but is unimplemented.
- `dedupe` dedupes rendered tensors, not support masks.
- `bernoulli` accepts mapping support by type but does not implement it.
- `path` accepts 4D points but only selects from `t=0`; `point` can use nonzero time.
- Predicate/callable params may not be serializable.

## `data/generate.py`

Target path: raw rollout moves to `ankos/src/ca/rollout.py`; shared boundary
logic belongs in `ankos/src/ca/boundary.py`.

Role: deterministic raw next-state rollout from a chosen dataset spec, initial state, and rule id.

Important dependencies:

- `torch`
- `dataclass`, `Mapping`, `Sequence`, `Any`
- `data.components.loci`
- `data.components.rules`

Top-level surface:

- dataclass: `Episode`
- public-ish functions: `generate_episode`, `rollout`, `canonical_coords`, `apply_boundary_read`, `apply_rule`
- internal helpers: `_rollout_ar2`, `_rollout_spatial_lookup`, `_next_spatial_state`, `_read_component`, `_channel_state`, `_apply_gate`, `_lookup_index`

Function notes:

- `Episode` stores dataset id, domain, rule id, shape, steps, states, optional coords, and metadata.
- `generate_episode` instantiates the rule, calls rollout, creates canonical coords, and returns an `Episode`.
- `rollout` dispatches by rule family; it ignores the frontier argument.
- `canonical_coords` returns time-major canonical coordinates through `loci`.
- `apply_boundary_read` reads one coordinate from a state with boundary behavior.
- `apply_rule` applies scalar/read-level AR2 or lookup logic.
- `_rollout_ar2` rolls a scalar sequence from two seed values.
- `_rollout_spatial_lookup` rolls 1D/2D/3D lookup rules synchronously and returns CPU states.
- `_next_spatial_state` computes one next spatial state.
- `_read_component` gathers selector-defined reads for every coordinate.
- `_channel_state` reduces component reads through exhaustive/totalistic/gate pipeline steps.
- `_apply_gate` applies binary comparisons/transforms to channel values.
- `_lookup_index` packs channel states into lookup indices.

Notable mismatches:

- Frontier/update schedule is part of the signature but not behavior.
- All spatial rules update full states synchronously.
- `_lookup_index` names inputs as bits, but channel values may be multi-valued.
- `generate_episode` always creates coords despite docstring implying optionality.
- Boundary handling setup is duplicated in multiple helpers.

## `data/tokenize.py`

Target path: next-state tokenization moves to `pe/components/tokenizer.py`.
Legacy text/BPE helpers have no Phase 1 target path.

Role: next-state episode vocabulary, layout, coordinate, serialization, target, and metadata layer, plus legacy autoresearch text-tokenizer compatibility.

Important dependencies:

- top-level: `torch`, `data.components.alphabets`, `data.components.loci`
- lazy legacy/runtime: `data.generate`, `prepare`, `pyarrow.parquet`, `rustbpe`, `tiktoken`, `pickle`, `os`, `sys`, `time`

Top-level surface:

- constants: pad/ignore/time sentinels, token type names/ids, attention/loss policy names, `SPECIAL_TOKENS`, BPE constants
- class: `Tokenizer`
- vocab/layout functions: `freeze_vocab`, `vocab`, `expand_vocab`, `serialization_plan`, `layout_id`, `canonical_position_coords`, `position_layouts_from_streams`, `position_ids_for_coords`
- transform functions: `stream_coordinate_transforms`, `normalize_transform`, `transform_id`, `apply_coordinate_transform`, scalarization helpers
- episode functions: `serialize_episode`, `build_next_state_targets`, `build_token_metadata`, `build_loss_metadata`, `mask_metadata`
- legacy text helpers: `text_iterator`, `train_tokenizer`, `get_token_bytes`

Function notes:

- `freeze_vocab` aliases `vocab`.
- `serialization_plan` builds per-dataset tokenization metadata from vocab.
- `layout_id` creates stable PE layout ids from dataset, shape, source-state count, and transform id.
- `canonical_position_coords` shifts real state times to model-facing `1..N` and optionally prepends one special coord.
- `position_layouts_from_streams` dedupes stream layouts and builds positions, scalar positions, and coord-to-id maps.
- `position_ids_for_coords` maps coords to layout-local ids.
- `apply_coordinate_transform` applies supported transforms to state rows while leaving special rows unchanged.
- `scalar_positions_for_coords` row-major scalarizes explicit coords for RoPE.
- `serialize_episode` converts raw episode values into input ids, targets, loss masks, coords, position ids, layout id, token type ids, time indices, and metadata.
- `build_next_state_targets`, `build_token_metadata`, `build_loss_metadata`, and `mask_metadata` expose pieces of serialized metadata.
- `vocab` builds a compact finite vocab recipe from dataset alphabets and special/domain tokens.
- `expand_vocab` materializes token/value maps from compact vocab.
- `Tokenizer` wraps legacy tiktoken encoding for text.
- `text_iterator`, `train_tokenizer`, and `get_token_bytes` implement old autoresearch-style BPE utilities.

Notable mismatches:

- Next-state tokenizer and legacy text tokenizer live in the same file.
- Docstring says this file should not own split logic or device movement; legacy helpers filter train/val and load token bytes to a device.
- Custom special tokens can be assigned ids but omitted from fixed `_special_metadata`.
- Position layout return objects contain tensors and tuple-key dicts, so persistence format is unclear.
- Transform identity uses only transform id, not full transform params.
- Coordinate transforms can touch time coordinates, despite mostly spatial naming.
- Raw time vs shifted model-facing time is easy to confuse.

## `model.py`

Target path: GPT composition stays in `pe/model.py`; attention execution moves
to `pe/components/attention.py`; optimizer code moves to
`pe/components/optimizer.py`.

Role: GPT-style transformer stack plus custom optimizer, wired to cached positional encodings.

Important dependencies:

- `torch`, `torch.nn`, `torch.nn.functional`
- `pe as pe_lib`
- optional `kernels.get_kernel` for FA3 at import time

Top-level surface:

- global: `fa3`
- dataclass: `GPTConfig`
- helpers: `norm`, `has_ve`, `apply_rotary_emb`
- modules: `CausalSelfAttention`, `MLP`, `Block`, `GPT`
- optimizer constants/functions/classes: `polar_express_coeffs`, `adamw_step_fused`, `muon_step_fused`, `MuonAdamW`

Function/class notes:

- `GPTConfig` stores model dimensions, context length, PE mode, and window pattern without validation.
- `norm` applies RMS norm over the last dimension.
- `has_ve` selects layers receiving value embeddings.
- `apply_rotary_emb` is a local split-half rotary helper, currently unused by model PE flow.
- `CausalSelfAttention` builds Q/K/V/proj layers, optional value-embedding gates, applies cached PE through `pe_lib`, normalizes Q/K, and uses FA3 when available/unmasked or SDPA fallback otherwise.
- `_attention_sdpa` repeats K/V for GQA and uses PyTorch SDPA; masks must include causality because `is_causal=False` when a mask exists.
- `MLP` is biasless 4x expansion with squared ReLU.
- `Block` is pre-norm attention plus pre-norm MLP residual block.
- `GPT` builds embeddings, blocks, LM head, value embeddings, residual scalars, window schedule, cache setter, FLOP/count helpers, optimizer grouping, and forward/loss path.
- `init_weights` is an explicit separate method that mutates parameters.
- `setup_optimizer` groups embedding/head/scalars for AdamW and matrix groups for Muon.
- `MuonAdamW` dispatches AdamW and Muon update kernels by group kind.

Notable mismatches:

- SDPA fallback ignores `window_size`; sliding-window semantics appear FA3-only unless encoded in external masks.
- `apply_rotary_emb` and `CausalSelfAttention.pe_mode` look stale/unused.
- `GPT.__init__` and `init_weights` disagree on initial scalar values unless `init_weights` is called.
- `set_pe_cache` validates only PE mode and head dim.
- `softcap = 15` is hard-coded.
- FA3 loading happens at import time on CUDA systems.

## `pe.py`

Target path: `pe/components/posenc.py`.

Role: positional-encoding math and cache-bundle layer for RoPE, axial RoPE, and MonSTER.

Important dependencies: `torch`; schema dependency on tokenizer-produced position layouts.

Top-level surface:

- constants: `ROPE_SCALE`, `MONSTER_BLOCK_DIM`, `MONSTER_TEMPORAL_SCALE`
- RoPE: `apply_rotary_emb`, `precompute_rotary_embeddings`, `precompute_rotary_embeddings_from_values`, `build_rope_cache`
- axial: `apply_axial_rotary_emb`, `precompute_axial_rotary_embeddings`, `build_axial_rope_cache`
- MonSTER: `apply_monster_emb`, `apply_monster_key_emb`, `precompute_monster_embeddings`, `build_monster_cache`
- router/cache: `coordinate_columns`, `build_cache_bundle`, `_build_layout_factors`, `apply_cached_position_encoding`, `_gather_factor`, `apply_position_encoding`

Function notes:

- `apply_rotary_emb` applies split-half RoPE to `[B,T,H,D]` tensors.
- `precompute_rotary_embeddings` builds sequential RoPE factors.
- `precompute_rotary_embeddings_from_values` builds RoPE factors from explicit scalar positions.
- `build_rope_cache` builds a legacy scaled sequential RoPE cache.
- `apply_axial_rotary_emb` applies axial factors to a rotary prefix and passes remaining channels through.
- `precompute_axial_rotary_embeddings` builds axial factors from coordinate columns.
- `build_axial_rope_cache` builds legacy meshgrid axial factors.
- `apply_monster_emb` applies the custom 12-channel MonSTER block transform.
- `apply_monster_key_emb` calls MonSTER with `time_sign=-1`.
- `precompute_monster_embeddings` builds MonSTER factors from 4D coords.
- `coordinate_columns` maps PE mode names to coordinate columns.
- `build_cache_bundle` builds current layout-keyed PE cache bundles.
- `_build_layout_factors` dispatches factor construction by PE mode.
- `apply_cached_position_encoding` is the current model-facing cached application path.
- `_gather_factor` gathers cached factors per row/layout/position id.
- `apply_position_encoding` is a legacy uncached helper.

Notable mismatches:

- Legacy helpers still generate implicit sequential/meshgrid positions despite docstring saying explicit cached positions.
- `build_rope_cache` returns `(length, cos, sin)` while legacy `apply_position_encoding` expects `(cos, sin)`.
- `seq_pos` is unused.
- `ROPE_SCALE` affects only legacy cache building, not current cache bundles.
- MonSTER factor application does not cast factors to Q/K dtype/device like RoPE/axial.
- Layout metadata stores positions as `.long()` even though factors are computed from floats.
- Cache metadata casts `base` to `int`.

## `prepare.py`

Target path: shared dataset preparation helpers move to `pe/data/datasets.py`;
dataset-specific preparation moves to `pe/data/<dataset>/prepare.py`.

Role: preparation/manifest-freezing CLI. It resolves configs and dataset specs, derives budgets, freezes vocab metadata, and writes deterministic source/train/eval artifacts under `data/datasets/<config_stem>/`.

Important dependencies:

- standard library: `argparse`, `hashlib`, `json`, `os`, `Counter`, dataclasses, `ceil`, `prod`, `Path`
- project: `data.tokenize`, `data.components.datasets`, `data.components.evals`

Top-level surface:

- constants: `CONFIG_DIR`, `OUTPUT_ROOT`, `TARGET_PARAM_DATA_RATIO`, `SPECIAL_TOKENS_PER_EPISODE`, `EVAL_EPISODES_PER_KIND`, `DATASET_FACTORIES`
- dataclasses: `EpisodeBudget`, `TokenWindowBudget`
- helpers/builders: `round_up`, `stable_hash64`, `stable_digest`, `json_ready`, `model_config`, `parameter_counts`, `training_targets`, `source_states_per_episode`, `token_window_budget`, `episode_budget`
- config/artifact functions: `config_path`, `read_json`, `atomic_write_json`, `validate_config`, `resolve_dataset_specs`
- manifest functions: `component_summary`, `seed_catalog_summary`, `dataset_catalog_digest`, `dataset_summary`, `shuffled_rule_ids`, `build_rule_pools`, `build_seed_streams`, `build_train_stream`, `build_eval_token_window`, `build_eval_streams`, `build_manifest_bundle`
- CLI: `prepare_config`, `print_summary`, `build_arg_parser`, `main`

Function notes:

- Budget dataclasses store per-dataset and per-window token/episode budgets.
- Stable hash/digest helpers produce deterministic seeds and catalog digests.
- `json_ready` converts dataclasses, mappings, sequences, callables, and shape/dtype-like objects to JSON-compatible values.
- `model_config` derives model dimensions from depth/max tokens.
- `parameter_counts` estimates parameter groups for budget scaling.
- `training_targets` computes target loss tokens from param/data ratio.
- `token_window_budget` computes how many source states/loss tokens fit in a serialized window.
- `episode_budget` computes episodes needed for target loss tokens.
- `validate_config` checks config shape and eval specs.
- `resolve_dataset_specs` maps dataset ids to factories.
- `build_rule_pools` hashes/shuffles rule ids and splits train/eval pools.
- `build_seed_streams` creates deterministic train/eval seed namespaces.
- `build_train_stream` and `build_eval_streams` write compact stream recipes.
- `build_manifest_bundle` produces manifest, vocab, train stream, and eval stream payloads.
- `prepare_config` reads config and writes the four JSON artifacts.

Notable mismatches:

- `special_tokens_per_episode` is configurable but manifest names are always `["<bos>", "<domain>"]`.
- Artifact writes are individually atomic, not transactionally atomic as a set.
- `dataset_catalog_digest` is a summary digest, not a full object digest.
- Eval spec validation happens twice.
- Rule count extraction is duplicated.
- `raw_states_per_episode = source_states + 1` can be confused with serialized states.

## `train.py`

Target path: training orchestration stays in `pe/train.py`; standalone
checkpoint evaluation belongs in `pe/eval.py`; checkpoint IO lives in
`pe/components/checkpoint.py`.

Role: phase-1 next-state training/eval CLI. It loads prepared artifacts, builds dataset specs, model config, PE cache bundle, runtime train batches, and optional eval/invariance metrics.

Important dependencies:

- `torch`
- `pe as pe_lib`
- `prepare`
- `data.batch`
- `data.tokenize`
- `model.GPT`, `model.GPTConfig`
- JSON artifacts under `data/datasets/<run_id>`

Top-level surface:

- constants: `DATASET_ROOT`, `SUPPORTED_EVAL_KINDS`, `DEFAULT_EVAL_KINDS`
- functions: `read_json`, `load_artifacts`, `dataset_specs_from_manifest`, `model_config_from_manifest`, `make_example_iterators`, `build_position_layouts`, `build_pe_cache`, `next_examples`, `evaluate_next_state`, `_row_loss_and_accuracy`, `evaluate_invariance_streams`, `train`, `build_arg_parser`, `main`

Function notes:

- `load_artifacts` loads source manifest, vocab, train streams, and eval streams.
- `dataset_specs_from_manifest` uses `prepare.resolve_dataset_specs`.
- `model_config_from_manifest` builds `GPTConfig` from manifest/vocab and selected PE mode.
- `make_example_iterators` creates train example iterators per stream.
- `build_position_layouts` delegates to tokenizer layout construction.
- `build_pe_cache` delegates to `pe.build_cache_bundle`.
- `next_examples` round-robins across stream iterators.
- `evaluate_next_state` builds eval position layouts/cache, temporarily swaps model cache, evaluates selected eval streams and invariance streams, then restores training mode/cache when present.
- `_row_loss_and_accuracy` computes per-row CE loss/correct/token counts.
- `evaluate_invariance_streams` evaluates original/transformed pairs and aggregates transformed-side metrics.
- `train` orchestrates artifact load, seed/device, model init, cache setup, AdamW optimizer, runtime batches, logging, and optional eval.
- `build_arg_parser` and `main` implement CLI.

Notable mismatches:

- Docstring says default invocation is conservative/CPU-ish, but parser defaults to CUDA when available.
- Eval schema compatibility is embedded as `kind`/`eval` fallback.
- Eval cache restore leaves eval cache installed if the original cache was `None`.
- Invariance transformed metrics divide by original token counts, relying on equal loss-token counts.
- Overall eval aggregate includes transformed invariance side only; original is comparison context.
- Empty eval behavior is inconsistent between zero-count streams and no selected streams.
- Training/eval duplicate loss/accuracy code.

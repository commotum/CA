# Evaluation Protocols and Metric IDs

This document defines the eval taxonomy for the v1 procedural next-state
benchmark. It is protocol-level: prompt lengths, target-window sizes, rollout
lengths, and larger OOD shapes are experiment parameters, not constants here.

The active runtime currently reports teacher-forced token NLL and token
accuracy. The state-level, episode-level, multi-step rollout, and full
geometry-consistency metrics below are target benchmark metrics to add where
they are not already implemented.

## Axes

### Domain

Use the integer domain code in metric ids.

| Code | Domain | Dataset |
| --- | --- | --- |
| `0D` | `t+0D` | `0d-ar2-97` |
| `1D` | `t+1D` | `1d-dyadrads` |
| `2D` | `t+2D` | `2d-dyadaxes` |
| `3D` | `t+3D` | `3d-dyadaxes` |

### Episode Relation

| Code | Meaning | Applies to |
| --- | --- | --- |
| `IN` | In-episode scoring: score predictions against targets from the same episode stream. | `RULE`, `SEED`, `HORIZON`, `SCALE`, `BOUNDARY` |
| `OUT` | Cross-episode or paired-view scoring: compare matched examples/views. | `INVARIANCE` |

The current invariance stream uses the same generated episode with two
coordinate views. It still belongs under `OUT` because the metric compares two
model-facing examples/views rather than one episode in isolation.

### Step Mode

This axis is required; otherwise teacher-forced and rollout metrics collide.

| Code | Meaning |
| --- | --- |
| `SS` | Single-step / teacher-forced. The model predicts with the actual history in context. |
| `MS` | Multi-step / rollout. The model predicts from its own generated history after the prompt. |

### Eval Code

| Code | Config eval | What changes |
| --- | --- | --- |
| `RULE` | `held-out-rule` | rule ids |
| `SEED` | `held-out-seed` | seed draws or seed family |
| `HORIZON` | `ood-horizon` | time horizon |
| `SCALE` | `ood-scale` | spatial scale |
| `BOUNDARY` | `ood-boundary` | boundary policy |
| `INVARIANCE` | `invariance` | coordinate frame |

### Distribution Regime

| Code | Eval codes |
| --- | --- |
| `HO` | `RULE`, `SEED` |
| `OOD` | `HORIZON`, `SCALE`, `BOUNDARY`, `INVARIANCE` |

`INVARIANCE` keeps its own eval code. It is classified under `OOD` because it
tests coordinate-frame generalization, but the eval name remains invariance.

### Level

| Code | Unit |
| --- | --- |
| `TOKEN` | One target token or cell. |
| `STATE` | One full target state. For `0D`, a state has one token. |
| `EPISODE` | The full evaluated target window for one example. |

### Metric

| Code | Meaning |
| --- | --- |
| `NLL` | Negative log likelihood for the unit at the selected level. |
| `ACCURACY` | Exact correctness for the unit at the selected level. |

For `STATE-NLL`, sum token NLLs within a state, then average over scored states.
For `EPISODE-NLL`, sum token NLLs over the evaluated target window, then average
over episodes. Keep `TOKEN-NLL` as the primary cross-shape comparison metric,
because total state and episode NLLs naturally grow with state size and horizon.

For `STATE-ACCURACY`, a state is correct only if every target token in that
state is correct. For `EPISODE-ACCURACY`, an episode is correct only if every
target state in the evaluated target window is correct.

## Canonical Metric ID

Use:

```text
[DOMAIN-INT]D-[IN/OUT]-[SS/MS]-[HO/OOD]-[EVAL-CODE]-[LEVEL-CODE]-[METRIC-CODE]
```

Examples:

```text
0D-IN-SS-HO-RULE-TOKEN-NLL
2D-IN-SS-OOD-HORIZON-STATE-ACCURACY
3D-IN-MS-OOD-SCALE-EPISODE-ACCURACY
2D-OUT-SS-OOD-INVARIANCE-TOKEN-NLL
3D-OUT-MS-OOD-INVARIANCE-STATE-NLL
```

## Config Coverage

| Config | Domains | Requested evals | Effective evals |
| --- | --- | --- | --- |
| `configs/v1-t+0d.json` | `0D` | `RULE`, `SEED`, `HORIZON`, `INVARIANCE` | `RULE`, `SEED`, `HORIZON` |
| `configs/v1-t+1d.json` | `1D` | all six evals | all six evals |
| `configs/v1-t+2d.json` | `2D` | all six evals | all six evals |
| `configs/v1-t+3d.json` | `3D` | all six evals | all six evals |
| `configs/v1-multi.json` | `0D`, `1D`, `2D`, `3D` | all six evals | `RULE`, `SEED`, and `HORIZON` for all domains; `SCALE`, `BOUNDARY`, and `INVARIANCE` for spatial domains only |

`prepare.py` filters `BOUNDARY` and `INVARIANCE` to non-scalar spatial domains.
`SCALE` is also spatial-only because it requires a configured larger shape.

## Eval Families

### RULE

Tests latent-rule generalization. The model trains on one rule-id pool and is
evaluated on rule ids reserved from that pool. The state space, seed
distribution, shape, boundary policy, and base horizon stay matched.

Domains:

- `0D`
- `1D`
- `2D`
- `3D`

Metric ids:

```text
[0D|1D|2D|3D]-IN-SS-HO-RULE-[TOKEN|STATE|EPISODE]-[NLL|ACCURACY]
[0D|1D|2D|3D]-IN-MS-HO-RULE-[TOKEN|STATE|EPISODE]-[NLL|ACCURACY]
```

### SEED

Tests initial-condition generalization with train-visible rule ids. The current
base version uses fixed unseen seed draws from the same seed catalog. If
explicit OOD seed families are added later, report the same metric ids with
additional seed-family or seed-bucket table columns.

Domains:

- `0D`
- `1D`
- `2D`
- `3D`

Metric ids:

```text
[0D|1D|2D|3D]-IN-SS-HO-SEED-[TOKEN|STATE|EPISODE]-[NLL|ACCURACY]
[0D|1D|2D|3D]-IN-MS-HO-SEED-[TOKEN|STATE|EPISODE]-[NLL|ACCURACY]
```

### HORIZON

Tests extrapolation along the time axis. The rule language, state space,
spatial shape, and boundary policy stay matched, while the evaluated trajectory
window is longer than the training window.

Domains:

- `0D`
- `1D`
- `2D`
- `3D`

Metric ids:

```text
[0D|1D|2D|3D]-IN-SS-OOD-HORIZON-[TOKEN|STATE|EPISODE]-[NLL|ACCURACY]
[0D|1D|2D|3D]-IN-MS-OOD-HORIZON-[TOKEN|STATE|EPISODE]-[NLL|ACCURACY]
```

### SCALE

Tests spatial-coordinate extrapolation. The model is evaluated on larger native
spatial shapes while keeping the same rule language and local update semantics.
This eval does not apply to `0D`.

Domains:

- `1D`
- `2D`
- `3D`

Metric ids:

```text
[1D|2D|3D]-IN-SS-OOD-SCALE-[TOKEN|STATE|EPISODE]-[NLL|ACCURACY]
[1D|2D|3D]-IN-MS-OOD-SCALE-[TOKEN|STATE|EPISODE]-[NLL|ACCURACY]
```

Useful breakdown columns:

- scale variant
- interior vs boundary band
- in-range vs beyond-training-coordinate region

### BOUNDARY

Tests boundary-policy extrapolation. Spatial domains train with the base
boundary policy and are evaluated under alternate boundary policies such as
fixed-one, periodic, and reflective reads. This eval does not apply to `0D`.

Domains:

- `1D`
- `2D`
- `3D`

Metric ids:

```text
[1D|2D|3D]-IN-SS-OOD-BOUNDARY-[TOKEN|STATE|EPISODE]-[NLL|ACCURACY]
[1D|2D|3D]-IN-MS-OOD-BOUNDARY-[TOKEN|STATE|EPISODE]-[NLL|ACCURACY]
```

Useful breakdown columns:

- boundary variant
- boundary band vs interior

### INVARIANCE

Tests whether predictions are stable under coordinate-frame transforms that
should preserve the underlying state evolution. Current streams use paired
original/transformed coordinate layouts for the same generated episode. A fuller
geometry-consistency eval should compare predictions after inverse-mapping the
transformed view back into the original frame.

This eval does not apply to `0D` in the prepared streams.

Domains:

- `1D`
- `2D`
- `3D`

Metric ids:

```text
[1D|2D|3D]-OUT-SS-OOD-INVARIANCE-[TOKEN|STATE|EPISODE]-[NLL|ACCURACY]
[1D|2D|3D]-OUT-MS-OOD-INVARIANCE-[TOKEN|STATE|EPISODE]-[NLL|ACCURACY]
```

Useful breakdown columns:

- transform id
- original metric value
- transformed metric value
- delta metric value
- inverse-mapped consistency error

For `INVARIANCE-ACCURACY`, report transformed accuracy and consistency
accuracy separately. Transformed accuracy asks whether the transformed view is
correct against target states. Consistency accuracy asks whether original and
transformed predictions agree after mapping into a common frame.

## Multidomain Gap

For `configs/v1-multi.json`, report each metric id by domain and eval family.
Also track the multidomain gap:

```text
multidomain gap =
  joint-training eval NLL
  - matched single-domain eval NLL
```

Compute this by domain, step mode, eval family, level, and metric where the
single-domain reference exists.

## Implementation Status

Currently implemented:

- `*-IN-SS-*-TOKEN-NLL`
- `*-IN-SS-*-TOKEN-ACCURACY`
- `*-OUT-SS-OOD-INVARIANCE-TOKEN-NLL` as original/transformed/delta values
- `*-OUT-SS-OOD-INVARIANCE-TOKEN-ACCURACY` as original/transformed/delta values

Still needed:

- state-level NLL and accuracy
- episode-level NLL and accuracy
- multi-step rollout scoring
- first-error position as a rollout diagnostic column
- calibrated horizon-cutoff reporting
- inverse-transform prediction consistency
- explicit OOD seed-family variants, if we want `SEED` to mean more than unseen
  seed RNG draws from the same seed catalog

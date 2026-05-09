# NumPy Target For Rollout Outputs

`ankos` should use NumPy-compatible raw arrays as the public rollout form
factor, while keeping a clean PyTorch handoff path for the PE experiment
harness.

## Recommendation

- Public rollout output should expose `states` as NumPy-style arrays.
- Batched states should use shape `(B, T, *spatial_shape)`.
- Unbatched states may use shape `(T, *spatial_shape)`.
- Coordinates should be integer arrays, either materialized as
  `(T * cell_count, 4)` or represented by layout metadata plus a helper that
  materializes canonical coordinates.
- Batchable inputs should be arrays where possible:
  - `rule_ids: (B,)`
  - `seed_states: (B, *spatial_shape)`
  - optional per-episode boundary/metadata arrays when needed later
- PE should convert at the harness boundary with `torch.from_numpy(...)` during
  batch construction.
- A future backend option such as `backend="numpy" | "torch"` can be added if
  GPU-resident rollout becomes important.

## Rationale

`ankos` is the generic cellular-automata package, not the PE training harness.
NumPy is the friendlier baseline for generic generation, tests, serialization,
CPU vectorization, and external use. It also keeps the public package lighter
and avoids making device/runtime policy part of the core CA API.

PyTorch is still the right representation inside PE because the model,
collation path, masks, and positional-encoding cache are all torch-native.
That does not require `ankos` itself to be PyTorch-first. The handoff can remain
explicit at the PE boundary.

The main reason to make rollout PyTorch-first would be if generation itself
becomes a training bottleneck and needs to stay GPU-resident. If that happens,
it should be treated as a backend optimization rather than the baseline API
contract.

The target shape is therefore:

```text
NumPy semantics as the public contract.
Backend-pluggable implementation if performance later requires it.
Torch conversion at the PE batch boundary.
```

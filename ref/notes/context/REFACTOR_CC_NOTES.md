## Bottom line

The true common core across **nanoGPT**, **nanochat**, and **autoresearch** is not “a ChatGPT stack” and not just “a GPT model.” It is a compact **causal language-model training substrate**:

> **A configurable GPT-like causal model + token stream batching + next-token loss + optimizer/schedule loop + validation/evaluation + simple artifact/experiment discipline.**

The three repos differ mostly in how much shell they build around that substrate:

| Repo             | Natural role in the set                                                                                                                                                                                       |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **nanoGPT**      | Minimal classic GPT pretraining/finetuning repo: `model.py`, `train.py`, configs, data prep, sampling.                                                                                                        |
| **nanochat**     | Full-stack LLM harness: tokenizer, pretraining, eval, SFT, RL, inference engine, checkpoints, web UI.                                                                                                         |
| **autoresearch** | Single-GPU autonomous experiment harness: fixed `prepare.py`, editable `train.py`, fixed-time runs, `val_bpb` hill-climbing. It explicitly says its training code is cherry-picked/simplified from nanochat.  |

The strongest reusable core is therefore **not** nanochat’s entire package and not autoresearch’s “single mutable file.” It is a small set of interfaces that allow the same causal-LM runtime to be used in different shells.

---

## 1. Natural categories of shared functionality

### A. Causal GPT model contract

**Coverage: all three.**

All three repos center on a GPT-style causal language model with a config object, token embeddings, a stack of Transformer blocks, an LM head, a forward pass that optionally computes cross-entropy loss, parameter/FLOP helpers, and in at least nanoGPT/nanochat, generation. nanoGPT’s analysis describes `GPTConfig`, `CausalSelfAttention`, `MLP`, `Block`, `GPT.forward`, `configure_optimizers`, `estimate_mfu`, and `generate` as core `model.py` responsibilities.  nanochat’s atlas similarly identifies `nanochat/gpt.py` as the central file defining model architecture, rotary/sliding-window attention, value embeddings, FLOP estimation, generation, and optimizer grouping.  autoresearch’s atlas maps the same core pieces inside its editable `train.py`: `GPTConfig`, attention, MLP, Block, GPT container, rotary cache, window sizing, parameter counting, FLOP estimation, and optimizer grouping. 

**Essential abstraction:** `CausalLM` with `forward(idx, targets=None, loss_reduction=...)`, `generate` optional, `estimate_flops`, `num_params/num_scaling_params`, and `setup_optimizer`.

**Implementation differences:**

| Repo             | Model style                                                                                                                                                                                                                               |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **nanoGPT**      | Classic GPT-2-like: learned absolute position embeddings, LayerNorm, optional bias, dropout, tied token/LM-head weights, fused QKV projection, GELU MLP.                                                                                  |
| **nanochat**     | Modern optimized GPT: RoPE, RMSNorm, no bias, untied embedding/head, separate Q/K/V, GQA support, QK norm, ReLU² MLP, sliding-window pattern, value embeddings, residual scalars, smear/backout, logit softcap, explicit dtype handling.  |
| **autoresearch** | Simplified single-file nanochat-derived model: RoPE, RMSNorm, GQA, sliding window, value embeddings, ReLU², Muon/AdamW grouping, but less full-stack machinery than nanochat.                                                             |

**Essential vs incidental:**
Essential: causal Transformer block, next-token logits, optional loss, model config, parameter/FLOP accounting.
Incidental: exact class names, whether QKV is fused, whether embeddings are tied, whether norm is LayerNorm or RMSNorm, whether RoPE or learned positions are used.

---

### B. Attention and positional machinery

**Coverage: all three for causal attention; nanochat + autoresearch for modern attention stack.**

All three implement causal self-attention. The stronger shared modern implementation is between **nanochat and autoresearch**: both use separate Q/K/V projections, grouped-query-compatible K/V heads, RoPE, QK normalization, sliding-window attention settings, and Flash Attention 3 style calls. nanochat’s `gpt.py` explicitly lists RoPE, QK norm, GQA, Flash Attention 3, no positional embeddings, and no learnable RMSNorm parameters as notable model features.  Autoresearch’s `train.py` has the same `GPTConfig` shape fields, `apply_rotary_emb`, GQA constraints, separate Q/K/V linears, QK RMSNorm, and FA3 call. 

**Candidate common core:** `AttentionSpec` and `PositionEncoding` hooks:

```text
AttentionSpec:
  n_head
  n_kv_head
  head_dim
  causal=True
  window_pattern optional
  backend: sdpa | fa3 | manual

PositionEncoding:
  learned_abs | rope
  build_cache(seq_len, head_dim, dtype, device)
  apply(q, k, positions/cache)
```

**Do not overfit the core to nanochat:** nanoGPT should still be able to use learned absolute position embeddings and standard SDPA. RoPE/GQA/sliding window should be a pluggable modern attention variant, not required by the base interface.

---

### C. Tokenization and token-stream construction

**Coverage: all three, with strongest nanochat + autoresearch overlap.**

All three repos transform text into integer token streams and produce `(x, y)` next-token training batches. The difference is where they draw the boundary:

| Repo             | Data representation                                                                                                                                                                                                                                                                                                                   |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **nanoGPT**      | Pre-tokenized `train.bin` / `val.bin`; random contiguous windows from NumPy memmaps; GPT-2 BPE or character vocab depending on dataset. nanoGPT’s `train.py` exposes `get_batch`, `estimate_loss`, and `get_lr`; its data prep writes binary token files.                                                                             |
| **nanochat**     | Parquet text shards, tokenizer trained separately, BOS-aligned best-fit packing, DDP-aware streaming, resume state. The atlas identifies `nanochat/dataloader.py` as owning BOS-aligned best-fit document packing and `nanochat/tokenizer.py` as owning tokenizer backends, special tokens, chat rendering, and token byte metadata.  |
| **autoresearch** | Fixed `prepare.py` owns data download, tokenizer training, runtime tokenizer wrapper, BOS-aligned best-fit dataloader, and BPB eval. The atlas calls `prepare.py` both setup script and fixed runtime library.                                                                                                                        |

**Essential abstraction:** a tokenizer interface plus a batch stream interface:

```text
Tokenizer:
  encode(text | list[text], prepend=None, append=None) -> list[int] | list[list[int]]
  decode(ids) -> str
  get_vocab_size() -> int
  get_bos_token_id() -> int
  optional encode_special()

BatchStream:
  next() -> x, y, state?
  x: LongTensor[B, T]
  y: LongTensor[B, T]
```

**Strong two-repo reusable core:** BOS-aligned best-fit packing from **nanochat + autoresearch**. It is foundational if the target core is modern pretraining, because it preserves document-boundary semantics while maintaining high utilization. Autoresearch’s `make_dataloader` does this in `prepare.py`, and nanochat’s `dataloader.py` does it in package form. 

**Essential vs incidental:**
Essential: `x,y` shifted next-token batches and a tokenizer boundary.
Incidental: whether data is memmap `.bin`, parquet text, Hugging Face dataset, GPT-2 BPE, RustBPE, or character-level.

---

### D. Training loop and schedule

**Coverage: all three.**

All three contain the same conceptual training loop:

```text
load config/artifacts
build model
build optimizer
build data stream
for steps/time:
  forward
  backward
  accumulate gradients
  schedule LR / optimizer params
  optimizer step
  zero grad
  periodically or finally evaluate
  log metrics
```

nanoGPT’s `train.py` supports scratch/resume/GPT-2 initialization, DDP, evaluation, checkpointing, LR scheduling, and logging.  Its training code configures optimizer, compile, DDP wrapping, `estimate_loss`, warmup+cosine LR, and checkpoint/eval flow.  nanochat’s `base_train.py` adds depth-derived sizing, scaling-law training horizon, FP8 option, BPB/CORE eval, sampling, checkpointing, DDP-aware accumulation, and Muon schedules.  Autoresearch keeps the loop single-GPU and wall-clock based; it stops after the fixed `TIME_BUDGET`, uses gradient accumulation, schedules LR/momentum/weight decay from time progress, runs final `evaluate_bpb`, and prints parseable summary metrics. 

**Essential abstraction:** `Trainer` should not know about “chat” or “agent hill-climbing.” It should know:

```text
Trainer:
  model
  optimizer
  train_loader
  evaluators
  schedules
  horizon: steps | tokens | flops | wall_clock
  callbacks: logging/checkpointing/sampling
```

**Implementation differences and tradeoffs:**

| Design choice | nanoGPT                                    | nanochat                                               | autoresearch              |
| ------------- | ------------------------------------------ | ------------------------------------------------------ | ------------------------- |
| Horizon       | Fixed iteration count                      | Param/data ratio, target FLOPs, or explicit iterations | Fixed wall-clock budget   |
| Config style  | Globals + `configurator.py` + config files | CLI args + shell recipes                               | Direct editable constants |
| Distributed   | DDP wrapper                                | Custom distributed optimizer/DDP-aware runtime         | Single GPU only           |
| Eval cadence  | Periodic train/val CE loss                 | BPB, CORE, sampling, checkpoints                       | Final fixed BPB           |
| Tradeoff      | Simple and teachable                       | Full experiment/product pipeline                       | Fast autonomous iteration |

---

### E. Optimizer grouping and optimizer implementation

**Coverage: all three for optimizer grouping; nanochat + autoresearch for Muon/AdamW split.**

nanoGPT groups parameters into decayed and non-decayed AdamW buckets and optionally uses fused AdamW. nanochat and autoresearch go further: they place embeddings, unembedding, value embeddings, and scalars into AdamW-style groups, while matrix parameters go to Muon groups. nanochat’s atlas explicitly notes that `GPT.setup_optimizer()` lives in `gpt.py`, so optimizer grouping is not isolated to `optim.py`.  Autoresearch’s atlas likewise identifies `setup_optimizer()` as the critical file-local control point and says it groups parameters into multiple AdamW and Muon buckets. 

**Candidate common core:** separate “parameter role discovery” from “optimizer math.”

```text
ParamGroups:
  embeddings
  unembedding
  transformer_matrices
  norms/scalars
  special_modules

OptimizerFactory:
  adamw_basic
  adamw_fused
  muon_adamw
  distributed_muon_adamw optional
```

**Essential vs incidental:**
Essential: parameter grouping belongs close to the model because it depends on architecture.
Incidental: exact LR values, betas, Muon coefficients, and whether Muon is enabled.

---

### F. Evaluation metrics

**Coverage: all three for validation loss; nanochat + autoresearch for BPB; nanochat-only for CORE/chat eval.**

All three evaluate language modeling quality. nanoGPT estimates mean train/val cross-entropy loss. nanochat and autoresearch use **bits per byte** as a tokenizer-vocab-size-independent metric; autoresearch’s `prepare.py` defines `evaluate_bpb` as the fixed ground-truth metric, using token byte lengths and excluding special tokens.  nanochat has `loss_eval.py` for BPB and `core_eval.py`/`base_eval.py` for CORE; its staged pipeline explicitly includes CORE, BPB, and sampling for base evaluation. 

**Candidate common core:**

```text
Evaluator:
  mean_loss(model, batch_iter, steps)
  bpb(model, batch_iter, token_bytes, steps)
  sample(model/tokenizer, prompts)
  optional external benchmark adapters
```

**Do not include in minimal core:** CORE task rendering, chat categorical/generative tasks, HumanEval execution, GSM8K reward, and ChatCORE. Those are nanochat’s evaluation surface, not the shared substrate.

---

### G. Model sizing, scaling, and compute accounting

**Coverage: all three, strongest nanochat + autoresearch.**

All three care about model size, token count, throughput, and MFU. nanoGPT exposes model parameter counting and MFU estimation in `model.py` and has scaling/sizing notebooks.  nanochat formalizes sizing around `--depth`: depth determines width, heads, training horizon, batch size, and scaling-law behavior. Its README describes depth as a single complexity dial that automatically determines other hyperparameters.  Autoresearch copies the depth/aspect-ratio/head-dim style and fixed-time reporting of FLOPs/MFU/params. 

**Candidate common core:**

```text
ModelSizer:
  from_depth(depth, aspect_ratio, head_dim, vocab_size, seq_len) -> GPTConfig

ComputeAccounting:
  num_params(model)
  num_scaling_params(model)
  flops_per_token(model)
  tokens_per_step(batch_size, seq_len, world_size, grad_accum)
  mfu(flops_per_step, dt, hardware_peak)
```

**Important distinction:** scaling analysis notebooks are not runtime core, but the **functions they motivate**—parameter counts, FLOP counts, token horizon, batch sizing—are reusable core.

---

### H. Configuration and experiment shell

**Coverage: all three in spirit; implementations differ sharply.**

The shared design choice is **flat, hackable, low-framework configuration**. The implementations diverge:

| Repo             | Config shell                                                                                          |
| ---------------- | ----------------------------------------------------------------------------------------------------- |
| **nanoGPT**      | `configurator.py` mutates globals from config files and `--key=value` overrides.                      |
| **nanochat**     | CLI args, run scripts, artifact directories, checkpoint metadata.                                     |
| **autoresearch** | Direct constants in `train.py`, fixed constants in `prepare.py`, and `program.md` agent instructions. |

Autoresearch’s `program.md` is not runtime Python, but it is part of the system: it instructs the agent to treat `prepare.py` as fixed, edit only `train.py`, run fixed 5-minute experiments, log `results.tsv`, and keep/discard commits by `val_bpb`. 

**Candidate common core:** do **not** standardize all repos onto one config system. Instead, keep the reusable code config-agnostic and let each shell provide config values.

```text
Common code accepts plain dataclasses/dicts.
Repo shells decide whether those come from:
  config.py
  argparse
  direct constants
  program.md/agent workflow
```

---

## 2. What is genuinely common, two-repo overlap, and repo-specific

### All three repos

These are safe candidates for the **essential common core**:

| Element                              | Why it is core                                                        |
| ------------------------------------ | --------------------------------------------------------------------- |
| GPT-style causal LM config           | Every repo defines model shape through a compact config object.       |
| Transformer block stack              | Attention + MLP + residual path is the central reusable architecture. |
| Next-token objective                 | All produce logits over vocab and train with shifted targets.         |
| Token batch stream                   | All ultimately yield `x, y` integer tensors for causal LM training.   |
| Training loop skeleton               | Forward/backward/accumulate/step/evaluate/log.                        |
| LR scheduling                        | Present in all, though schedule shape differs.                        |
| Parameter/FLOP/throughput accounting | Present in all, with different sophistication.                        |
| Minimal hackable PyTorch style       | All avoid heavyweight framework abstractions.                         |

### nanochat + autoresearch

These are strong **modern pretraining-core** candidates:

| Element                                      | Why it matters                                                   |
| -------------------------------------------- | ---------------------------------------------------------------- |
| RoPE + RMSNorm + no-bias modern GPT          | Shared directly; foundational for current nanochat/autoresearch. |
| GQA-compatible Q/K/V split                   | Core architectural assumption in both.                           |
| Sliding-window attention pattern             | Both expose `window_pattern`.                                    |
| Value embeddings                             | Shared architecture component.                                   |
| ReLU² MLP                                    | Shared MLP choice.                                               |
| Depth-derived sizing                         | `depth -> model_dim -> heads` pattern appears in both.           |
| Muon + AdamW split optimizer                 | Foundational optimization overlap.                               |
| BOS-aligned best-fit dataloader              | Shared data packing strategy.                                    |
| RustBPE/tiktoken tokenizer + token bytes     | Shared tokenizer/eval substrate.                                 |
| BPB evaluation                               | Core metric in both.                                             |
| Compile + BF16/H100-oriented throughput loop | Shared performance assumption, though nanochat is more portable. |

### nanoGPT + nanochat

These are strong **general reusable repo-design** candidates:

| Element                                       | Why it matters                                                                                                                                                |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Model code separated from training entrypoint | nanoGPT has `model.py` + `train.py`; nanochat has `nanochat/gpt.py` + `scripts/base_train.py`. Autoresearch intentionally collapses this.                     |
| Checkpoint/resume flow                        | nanoGPT checkpointing is simple; nanochat checkpoint manager is robust. Autoresearch intentionally avoids checkpointing as an experiment-loop simplification. |
| Sampling/generation path                      | nanoGPT has `sample.py` and `GPT.generate`; nanochat has `GPT.generate` plus `Engine`.                                                                        |
| DDP/multi-GPU support                         | Present in nanoGPT and nanochat, absent in autoresearch.                                                                                                      |
| Configurable training scripts                 | nanoGPT uses config files/overrides; nanochat uses CLI args/run scripts.                                                                                      |

### nanoGPT + autoresearch

This overlap is weaker but still meaningful:

| Element                                                | Why it matters                                                                                       |
| ------------------------------------------------------ | ---------------------------------------------------------------------------------------------------- |
| Extremely small, hackable training surface             | nanoGPT is minimal by design; autoresearch intentionally keeps only a few files.                     |
| Single main training script as primary editing surface | nanoGPT’s `train.py` is central; autoresearch’s `train.py` is explicitly the editable research file. |
| Simple local experiment feedback loop                  | nanoGPT via configs and runs; autoresearch via fixed-time hill-climbing.                             |

### nanochat-specific

These should **not** be in the minimal common core:

| Element                              | Why repo-specific                                                               |
| ------------------------------------ | ------------------------------------------------------------------------------- |
| Chat SFT/RL stages                   | Only nanochat has the full staged chat pipeline.                                |
| `tasks/` abstraction                 | Useful for nanochat, not common to nanoGPT/autoresearch.                        |
| CORE/ChatCORE benchmark internals    | nanochat-specific eval surface.                                                 |
| KV-cache `Engine` with tool handling | nanochat inference product/runtime feature.                                     |
| Web UI / FastAPI serving             | nanochat-only.                                                                  |
| Report card generator                | nanochat artifact/reporting layer.                                              |
| Sandboxed code execution             | nanochat task/eval feature.                                                     |
| FP8 conversion utilities             | nanochat-specific module, though conceptually related to speedrun optimization. |

### autoresearch-specific

These should remain outside the reusable core:

| Element                                | Why repo-specific                                                     |
| -------------------------------------- | --------------------------------------------------------------------- |
| `program.md` autonomous agent protocol | Workflow/control-plane, not model runtime.                            |
| Fixed 5-minute wall-clock budget       | Central to autoresearch, but not general training.                    |
| Keep/discard by git commit             | Research workflow artifact, not reusable LM core.                     |
| “Only edit `train.py`” rule            | Intentional simplification, not a reusable software design principle. |
| No checkpointing during training       | A deliberate tradeoff for short experiments.                          |

### nanoGPT-specific

These are mostly historical/minimal GPT-2 reproduction choices:

| Element                                | Why repo-specific or legacy                                                              |
| -------------------------------------- | ---------------------------------------------------------------------------------------- |
| GPT-2 weight import via Hugging Face   | Useful, but specific to nanoGPT’s reproduction/finetune goal.                            |
| Learned absolute positional embeddings | Core to nanoGPT, but not common with nanochat/autoresearch.                              |
| Tied token embedding / LM head         | nanoGPT-specific here.                                                                   |
| Memmap `.bin` random-window loader     | Very simple and useful, but not shared with nanochat/autoresearch’s parquet/BOS packing. |
| Character-level Shakespeare path       | Demo/debug path, not common core.                                                        |
| `configurator.py` global mutation      | A nanoGPT style choice, not an abstraction to preserve.                                  |

---

## 3. Meaningful implementation differences and tradeoffs

### Classic simplicity vs modern optimized architecture

nanoGPT’s model is easier to read and closer to GPT-2. It is a good pedagogical/common baseline. nanochat/autoresearch are more specialized for fast modern small-model pretraining: RoPE, RMSNorm, GQA, ReLU², value embeddings, sliding windows, and Muon. The reusable core should allow both, rather than “upgrade” nanoGPT into nanochat.

### Pre-tokenized random windows vs document-aware packing

nanoGPT’s memmap random-window loader is minimal and fast once data is prepared. nanochat/autoresearch’s BOS-aligned best-fit packing is more complex but carries document boundary assumptions and supports tokenizer/dataset changes more cleanly. For a reusable core, the right abstraction is not “one dataloader”; it is a `BatchStream` interface with multiple implementations.

### Step-count training vs token/FLOP/wall-clock horizons

nanoGPT thinks mainly in iterations. nanochat thinks in tokens, params, FLOPs, depth, and scaling-law horizons. Autoresearch thinks in fixed wall-clock experiments. A common `TrainingHorizon` abstraction should support all three:

```text
steps
tokens
flops
wall_clock_seconds
```

### AdamW-only vs split optimizer

nanoGPT’s AdamW grouping is broadly reusable and simple. nanochat/autoresearch’s Muon+AdamW split is a strong modern overlap, but it is too opinionated to be mandatory. The common core should expose parameter roles and let the shell choose the optimizer factory.

### Product/eval stack vs experiment stack

nanochat’s `Engine`, checkpoint manager, CORE eval, chat tasks, RL, and web UI are valuable, but they are not shared with nanoGPT/autoresearch. They should sit above the common core as optional modules.

---

## 4. Minimal reusable common core proposal

A minimal common core should be a **small library**, not a framework. It should preserve the “readable/hackable” style while preventing duplication of the truly shared pieces.

### Proposed module layout

```text
common_core/
  model.py
  attention.py
  tokenizer.py
  data.py
  optim.py
  schedules.py
  eval.py
  sizing.py
  checkpoint.py
  train_runtime.py
```

### `model.py`

Responsibilities:

```text
GPTConfig
CausalLM / GPT
Block
MLP
model.forward(idx, targets=None, loss_reduction="mean")
model.estimate_flops()
model.num_scaling_params()
model.setup_optimizer(...)
optional model.generate(...)
```

Design:

* Keep the base class generic enough for nanoGPT-style and nanochat-style GPTs.
* Put architecture variants behind config flags or small injected components, not large framework registries.
* Do not include chat formatting, SFT masks, RL rewards, or web serving.

### `attention.py`

Responsibilities:

```text
AttentionSpec
apply_rotary_emb
build_rope_cache
causal_sdpa_attention
optional flash_attn adapter
optional sliding_window support
```

Design:

* Base support: standard causal attention.
* Optional support: RoPE, GQA, FA3, KV cache, sliding windows.
* Keep nanoGPT learned position embeddings possible by not requiring RoPE.

### `tokenizer.py`

Responsibilities:

```text
TokenizerProtocol:
  encode
  decode
  get_vocab_size
  get_bos_token_id
  encode_special optional

RustBPETokenizer
TiktokenTokenizer
CharTokenizer optional
token_bytes builder
```

Design:

* Include token byte lookup because it is required for BPB and appears as foundational in nanochat/autoresearch.
* Keep chat serialization out of the base tokenizer; nanochat can extend it.

### `data.py`

Responsibilities:

```text
DatasetSource:
  BinMemmapSource
  ParquetTextSource

BatchStream:
  random_window_loader
  bos_bestfit_loader
  optional distributed shard state
```

Interface:

```python
batch = next(loader)
# either:
x, y = batch
# or:
x, y, state = batch
```

Design:

* Preserve nanoGPT’s simple memmap loader.
* Preserve nanochat/autoresearch’s BOS best-fit loader.
* State/resume should be optional, because autoresearch does not need checkpoint resume but nanochat does.

### `optim.py`

Responsibilities:

```text
build_param_groups(model, policy)
AdamW factory
MuonAdamW optional
DistMuonAdamW optional
```

Design:

* The core reusable part is **parameter-role grouping**, not any one optimizer.
* Support:

  * `adamw_by_dim` for nanoGPT.
  * `adamw_muon_by_role` for nanochat/autoresearch.
* Keep optimizer schedules in `schedules.py`.

### `schedules.py`

Responsibilities:

```text
cosine_warmup_decay
linear_warmup_constant_warmdown
time_budget_progress
muon_momentum_schedule
weight_decay_schedule
```

Design:

* Schedule functions should be pure.
* Let training shells decide whether progress is based on step, token, FLOP, or wall clock.

### `eval.py`

Responsibilities:

```text
estimate_loss
evaluate_bpb
sample_prompts optional
```

Design:

* `evaluate_bpb` should accept `token_bytes` and a loader.
* CORE/chat eval should not live here; nanochat can keep those as upper-layer benchmark adapters.

### `sizing.py`

Responsibilities:

```text
build_gpt_config_from_depth(depth, aspect_ratio, head_dim, seq_len, vocab_size)
count_params_by_group
estimate_flops_per_token
compute_tokens_per_step
compute_grad_accum_steps
optional batch-size scaling
```

Design:

* This module captures the real overlap among nanoGPT’s sizing notebooks, nanochat’s scaling-law machinery, and autoresearch’s depth/time-budget reporting.
* Keep specific empirical constants outside or injectable.

### `checkpoint.py`

Responsibilities:

```text
save_checkpoint
load_checkpoint
strip_compile_prefix
save_metadata
optional optimizer shard IO
```

Design:

* Provide a minimal checkpoint format for nanoGPT/nanochat-style use.
* Let autoresearch opt out.
* Do not force nanochat’s full `base/sft/rl` directory mapping into the common core.

### `train_runtime.py`

Responsibilities:

```text
compute/device init
dtype selection
torch.compile hook
gradient accumulation helper
metric logging callback interface
```

Design:

* This should be thin.
* Do not build a large Trainer framework.
* Expose helper functions that `train.py`, `scripts/base_train.py`, and autoresearch’s single-file loop can call or inline.

---

## 5. Proposed interface sketch

```python
@dataclass
class TrainBatch:
    x: torch.Tensor
    y: torch.Tensor
    state: dict | None = None

class TokenizerProtocol:
    def encode(self, text, prepend=None, append=None): ...
    def decode(self, ids): ...
    def get_vocab_size(self) -> int: ...
    def get_bos_token_id(self) -> int: ...

class BatchStream:
    def __iter__(self): return self
    def __next__(self) -> TrainBatch: ...

class CausalLM(nn.Module):
    config: GPTConfig
    def forward(self, idx, targets=None, loss_reduction="mean"): ...
    def estimate_flops(self) -> float: ...
    def num_scaling_params(self) -> dict: ...
    def setup_optimizer(self, policy, **kwargs): ...

class Evaluator:
    def evaluate_loss(self, model, loader, steps): ...
    def evaluate_bpb(self, model, loader, token_bytes, steps): ...
```

This is enough to express the real common runtime:

```python
tokenizer = load_tokenizer(...)
loader = make_loader(source, tokenizer, batch_size=B, seq_len=T, packing="bos_bestfit")
model = GPT(model_cfg).to(device)
optimizer = model.setup_optimizer(policy="adamw_muon_by_role")

for step in horizon:
    x, y, state = next(loader)
    loss = model(x, y)
    loss.backward()
    optimizer.step()
    optimizer.zero_grad(set_to_none=True)
```

---

## 6. What I would include in the “candidate common core”

Include these:

1. **GPT model interface and base implementation**
2. **Attention/position abstraction**
3. **Tokenizer protocol**
4. **`x,y` batch-stream protocol**
5. **Random-window and BOS-best-fit dataloaders**
6. **Cross-entropy and BPB evaluators**
7. **Parameter grouping policies**
8. **AdamW and optional MuonAdamW optimizer factories**
9. **Schedule helpers**
10. **Model sizing/FLOP/MFU utilities**
11. **Minimal checkpoint helpers**
12. **Thin runtime helpers for device/dtype/compile/gradient accumulation**

Keep these outside the minimal common core:

1. nanochat web UI
2. nanochat chat tasks/SFT/RL
3. nanochat CORE internals, except maybe as optional plugin
4. nanochat `Engine` except as optional inference extension
5. autoresearch keep/discard git workflow
6. autoresearch fixed 5-minute rule
7. nanoGPT GPT-2 import path, except as optional compatibility feature
8. One mandated config system

---

## 7. Final synthesis

The **essential common core** is:

```text
causal LM model
+ tokenization boundary
+ token batch stream
+ next-token loss/eval
+ optimizer/schedule loop
+ sizing/compute accounting
+ lightweight artifacts
```

The **strong modern two-repo core** from nanochat + autoresearch is:

```text
RoPE/RMSNorm/GQA/sliding-window GPT
+ BOS best-fit parquet/tokenizer loader
+ BPB metric
+ Muon/AdamW role-based optimizer
+ depth-derived sizing
```

The **strong repo-structure two-repo core** from nanoGPT + nanochat is:

```text
separate model code from training entrypoint
+ checkpoint/resume
+ sampling/generation
+ optional DDP
+ config-driven train scripts
```

The minimal reusable design should combine those without importing nanochat’s full product stack or autoresearch’s agent workflow. It should look closer to:

```text
model.py
attention.py
tokenizer.py
data.py
optim.py
schedules.py
eval.py
sizing.py
checkpoint.py
```

not:

```text
nanochat’s whole package
```

and not:

```text
one giant mutable train.py
```

That is the natural common core the repo contents point to.

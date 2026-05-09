The four conventions are best understood as **what the time index is attached to**.

| Convention                                   |                      Canonical form | Index (t) refers to                                 | Who uses it                                                       | Why                                                                                            |
| -------------------------------------------- | ----------------------------------: | --------------------------------------------------- | ----------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| **1. Target-relative / label-indexed**       |                (p(x_t \mid x_{<t})) | The token/event being predicted                     | Language-model probability theory, autoregressive modeling papers | Clean for writing likelihoods and sequence factorizations                                      |
| **2. State-relative / context-indexed**      |           (h_t \rightarrow x_{t+1}) | The current state/representation after seeing (x_t) | Transformer implementations, generation loops                     | Matches arrays, logits, KV cache, and “given current context, predict next token”              |
| **3. Dynamical update / transition-indexed** |                    (s_{t+1}=F(s_t)) | The current system state being updated              | Wolfram, cellular automata, dynamical systems                     | Natural when the rule is an update law from one full state/row to the next                     |
| **4. Prediction-time / agent-time indexed**  | (y_t \leadsto z_t(o_{t+1},y_{t+1})) | The time a prediction is made                       | Sutton, TD learning, reinforcement learning                       | Natural when an agent makes a prediction now, then later receives information used to train it |

## 1. Target-relative convention

This is the most common **formal probability** convention for autoregressive models:

[
p(x_{1:T})=\prod_{t=1}^{T}p(x_t\mid x_{<t})
]

Here, the index (t) belongs to the **target**.

So the model is described as predicting:

[
x_t
]

from:

[
x_1,\dots,x_{t-1}
]

This convention is common in mathematical descriptions of language modeling because it makes the probability factorization clean. Each term in the product is “the probability of the token at position (t), conditioned on all previous tokens.”

In this convention, saying “the prediction at time (t)” often means:

[
\text{predict the token whose index is }t
]

not “use the state at index (t).”

So:

[
\boxed{\text{target-relative: predict }x_t\text{ from }x_{<t}}
]

## 2. State-relative convention

This is the common **implementation / transformer-internals** convention:

[
h_t=f(x_{\le t})
]

[
p(x_{t+1}\mid x_{\le t})=\text{softmax}(Wh_t)
]

Here, the index (t) belongs to the **current context/state**.

The hidden state at position (t) has seen tokens through (x_t), so its job is to predict the **next** token:

[
x_{t+1}
]

This is the convention you usually see when discussing GPT generation:

[
x_1,\dots,x_t \longrightarrow x_{t+1}
]

or implementation details like shifted logits and labels:

[
\text{logits at position }t \rightarrow \text{label }x_{t+1}
]

This convention is used because it matches how the computation is actually arranged. The model processes an input position, produces logits at that position, and those logits are trained against the following token.

So:

[
\boxed{\text{state-relative: state at }t\text{ predicts }x_{t+1}}
]

## 3. Wolfram’s dynamical-update convention

Wolfram’s cellular automaton convention is a version of the **state-relative update convention**, but it is not framed as prediction. It is framed as **evolution**.

The natural form is:

[
s_{t+1}=F(s_t)
]

or for an individual cell:

[
a_i(t+1)=F(a_{i-1}(t),a_i(t),a_{i+1}(t))
]

In Wolfram’s notation, this often appears as a prime:

[
a_i'=\operatorname{Mod}[a_{i-1}+a_{i+1},2]
]

where (a_i') means the **new value** of the cell after applying the rule. In explicit temporal indexing:

[
a_i(t+1)=\operatorname{Mod}[a_{i-1}(t)+a_{i+1}(t),2]
]

So Wolfram’s convention is:

[
\boxed{\text{current row/state }t\text{ determines next row/state }t+1}
]

This matches cellular automata because the central object is not a probabilistic prediction but a deterministic update rule. The rule says: given the current configuration, compute the next configuration. Wolfram describes cellular automata as rows/steps where each row is produced from the previous one; the rule table gives the new color of the center cell on the next step from the previous neighborhood. 

This is closest to:

[
h_t \rightarrow x_{t+1}
]

rather than:

[
p(x_t\mid x_{<t})
]

But in cellular automata, (h_t) is not a learned hidden state. It is simply the whole current system configuration.

## 4. Sutton’s prediction-time convention

Sutton’s TD-network convention is also state-relative, but with reinforcement-learning timing.

The prediction vector is indexed by when the prediction is made:

[
\mathbf{y}_t
]

The paper defines the prediction update as:

[
\mathbf{y}*t=\mathbf{u}(\mathbf{y}*{t-1},a_{t-1},o_t,\mathbf{W}_t)
]

So (\mathbf{y}_t) is the prediction available at time (t), after receiving observation (o_t). Its TD target is:

[
\mathbf{z}*t=\mathbf{z}(o*{t+1},\tilde{\mathbf{y}}_{t+1})
]

So the target for the prediction made at time (t) uses next-step information: (o_{t+1}) and/or (\mathbf{y}_{t+1}). Sutton also gives the computation order as:

[
\mathbf{y}*t,\ a_t,\ \mathbf{c}*t,\ o*{t+1},\ \mathbf{x}*{t+1},\ \tilde{\mathbf{y}}*{t+1},\ \mathbf{z}*t,\ \mathbf{W}*{t+1},\ \mathbf{y}*{t+1}
]

which makes the timing explicit. 

So Sutton’s convention is:

[
\boxed{\text{prediction }y_t\text{ is made at time }t,\text{ then trained using a target involving }t+1}
]

For a simple one-step prediction:

[
y_t \approx \mathbb{E}[o_{t+1}\mid \text{history through }t]
]

This is not target-relative. Sutton does **not** generally index the prediction by the future event being predicted. He indexes it by the time at which the agent has the information and makes the prediction.

## The deeper distinction

The four conventions reduce to two big families:

[
\textbf{Target-indexed}
]

versus

[
\textbf{source/state/prediction-time indexed}
]

The target-indexed convention says:

[
\text{the thing with index }t\text{ is what we are trying to predict}
]

The state-indexed convention says:

[
\text{the thing with index }t\text{ is what we currently know}
]

That gives the central difference:

[
p(x_t\mid x_{<t})
]

versus:

[
p(x_{t+1}\mid x_{\le t})
]

They are mathematically equivalent under an index shift, but they emphasize different things.

## Why different fields prefer different conventions

Probability theory tends to use target-relative notation because it wants to factor a joint distribution:

[
p(x_1,\dots,x_T)
]

into terms indexed by the variable being predicted:

[
p(x_t\mid x_{<t})
]

Transformer implementation tends to use state-relative notation because the computation happens at positions:

[
h_t=f(x_{\le t})
]

and the logits at position (t) are trained against the next token:

[
x_{t+1}
]

Cellular automata use update notation because the object of interest is not a prediction but an evolution rule:

[
s_t\mapsto s_{t+1}
]

TD learning uses prediction-time notation because the object of interest is an agent making predictions over time. The prediction is indexed by when the agent makes it, and the learning target is constructed afterward from later observations and later predictions.

## Mapping them to one another

For GPT-style autoregression:

[
\underbrace{p(x_t\mid x_{<t})}_{\text{target-relative}}
]

is the same relationship as:

[
\underbrace{h_{t-1}\rightarrow x_t}_{\text{state-relative}}
]

or equivalently:

[
\underbrace{h_t\rightarrow x_{t+1}}_{\text{state-relative, shifted}}
]

For Wolfram-style cellular automata:

[
s_t\rightarrow s_{t+1}
]

For Sutton-style TD prediction:

[
y_t\rightarrow z_t(o_{t+1},y_{t+1})
]

The closest analogy among the four is:

[
\text{GPT implementation: } h_t\rightarrow x_{t+1}
]

[
\text{Wolfram: } s_t\rightarrow s_{t+1}
]

[
\text{Sutton: } y_t\rightarrow z_t\text{ involving }t+1
]

The odd one out is the formal language-model factorization:

[
p(x_t\mid x_{<t})
]

because it indexes by the **target** rather than the **current state**.

## Practical recommendation

Use both indices explicitly whenever ambiguity matters:

[
\text{state at time }t:\quad s_t
]

[
\text{target generated next:}\quad x_{t+1}
]

[
\text{prediction made now:}\quad \hat{x}_{t+1|t}
]

That last notation is especially clear:

[
\hat{x}_{t+1|t}
]

means:

> a prediction, made using information through time (t), of the quantity at time (t+1).




## 1. Target-relative / label-indexed convention

[
p(x_{1:T})=\prod_{t=1}^{T}p(x_t\mid x_{<t})
]

Here, (t) indexes the **thing being predicted**.

[
\boxed{\text{predict }x_t\text{ from }x_{<t}}
]

Used by: **autoregressive probability theory, language-model likelihood derivations.**

Why: it cleanly factors a sequence distribution by indexing each conditional probability by its target variable.

---

## 2. State-relative / context-indexed convention

[
h_t=f(x_{\le t})
]

[
p(x_{t+1}\mid x_{\le t})=\text{softmax}(Wh_t)
]

Here, (t) indexes the **current state/context**.

[
\boxed{\text{state at }t\text{ predicts }x_{t+1}}
]

Used by: **GPT-style transformer implementations, generation loops, shifted-logit training descriptions.**

Why: it matches the actual computation: the representation/logits at position (t) are trained against the next token (x_{t+1}).

---

## 3. Dynamical update / transition-indexed convention

[
s_{t+1}=F(s_t)
]

or for cellular automata:

[
a_i(t+1)=F(a_{i-1}(t),a_i(t),a_{i+1}(t))
]

Here, (t) indexes the **current system state**, and the rule produces the next state.

[
\boxed{\text{state at }t\rightarrow\text{state at }t+1}
]

Used by: **Wolfram’s cellular automata and dynamical systems descriptions.**

Why: the rule is not framed as prediction; it is framed as evolution. Wolfram describes each row/step as being generated from the previous row/step, with the rule giving the new cell color from the previous neighborhood. 

---

## 4. Prediction-time / agent-time convention

[
\mathbf{y}*t=\mathbf{u}(\mathbf{y}*{t-1},a_{t-1},o_t,\mathbf{W}_t)
]

[
\mathbf{z}*t=\mathbf{z}(o*{t+1},\tilde{\mathbf{y}}_{t+1})
]

Here, (t) indexes the **time the prediction is made**, not the future target time.

[
\boxed{\text{prediction }y_t\text{ is made at }t,\text{ then trained using information from }t+1}
]

Used by: **Sutton’s TD networks and reinforcement-learning temporal-difference notation.**

Why: the agent makes a prediction at time (t), acts, receives later information, and then constructs the TD target (z_t) from (o_{t+1}) and/or (\mathbf{y}_{t+1}). 

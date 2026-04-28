# Cellular Automata Episode / Trajectory Generator Schema

This schema defines a full-state trajectory generator for explicit $t+N\mathrm{D}$ domains with $N \in \{0,1,2,3\}$.

Every token, cell, voxel, or scalar state is addressed by a canonical four-coordinate vector

$$
c = [t,x,y,z] \in \mathbb{Z}^4.
$$

Unused spatial axes are set to zero. Thus:

$$
\begin{aligned}
t+0\mathrm{D}:&\quad c=[t,0,0,0],\\
t+1\mathrm{D}:&\quad c=[t,x,0,0],\\
t+2\mathrm{D}:&\quad c=[t,x,y,0],\\
t+3\mathrm{D}:&\quad c=[t,x,y,z].
\end{aligned}
$$

At construction round $k$, `FRONTIER` selects which coordinates are writable. `RULE` is applied in parallel to all writable coordinates using timestep-causal reads from `NEIGHBORHOOD`. All non-frontier coordinates are copied through unchanged.

---

## Specification

```text
SPECIFICATION:
    DOMAIN
    SHAPE
    ALPHABET
    SEED
    BOUNDARY
    NEIGHBORHOOD = (NEIGHBORHOOD[1], ..., NEIGHBORHOOD[m])
    FRONTIER = (FRONTIER[1], ..., FRONTIER[q])
    RULE
```

Each neighborhood is specified as a relative-offset read selector built from the shared selector/mask utility:

```text
NEIGHBORHOOD[j]:
    SELECTOR[Q_N, C_N]
    Q_N = Z⁴
    C_N = (c, k, X̃⁽ᵏ⁾)
    VARIABLE = δ = [Δt, Δx, Δy, Δz]
    FRAME = RELATIVE_TO_TARGET
    UNIVERSE = Ω_j : C_N → finite subsets of Z⁴
    PREDICATE = (η_j,1, ..., η_j,n)
    COMBINE = Ψ_j
    ORDER = ord_j
    READ_MODE ∈ {COMPACT_SELECTED, FIXED_SUPPORT_WITH_MASK}
```

Each frontier component is specified as an absolute-coordinate write selector built from the same selector/mask utility:

```text
FRONTIER[i]:
    SELECTOR[Q_F, C_F]
    Q_F = D
    C_F = (k, X̃⁽ᵏ⁾)
    VARIABLE = c = [t, x, y, z]
    FRAME = ABSOLUTE
    UNIVERSE = U_i : C_F → finite subsets of D
    PREDICATE = (φ_i,1, ..., φ_i,n)
    COMBINE = Φ_i
    ORDER = ord_i
```

The rule type is selected from:

$$
\mathrm{RULETYPE} \in
\begin{aligned}[t]
&\mathrm{EXHAUSTIVE},\\
&\mathrm{ISOTROPIC},\\
&\mathrm{SEMI\text{-}TOTALISTIC},\\
&\mathrm{TOTALISTIC},\\
&\mathrm{FORMULAIC},\\
&\mathrm{STOCHASTIC}
\end{aligned}
$$

---

## State

A generated episode is a persistent trajectory field

$$
X:D\to A.
$$

During generation, the partially written trajectory after construction round $k$ is

$$
X^{(k)}:D\to A.
$$

All reads at round $k$ are taken from a single boundary-extended snapshot

$$
\widetilde{X}^{(k)}:\mathbb{Z}^4\to A.
$$

The construction round $k$ is an evaluator index, not an additional coordinate axis. The persistent schedule coordinate is always the explicit coordinate $t$ inside

$$
c=[t,x,y,z].
$$

---

## DOMAIN

`DOMAIN` fixes the active dimensionality while retaining the canonical four-coordinate address.

Let

$$
d_s\in\{0,1,2,3\}
$$

be the number of active spatial axes.

The active coordinate sets are:

$$
\begin{aligned}
t+0\mathrm{D}:&\quad [t,0,0,0],\\
t+1\mathrm{D}:&\quad [t,x,0,0],\\
t+2\mathrm{D}:&\quad [t,x,y,0],\\
t+3\mathrm{D}:&\quad [t,x,y,z].
\end{aligned}
$$

The full persistent domain is always a subset of $\mathbb{Z}^4$:

$$
D\subseteq\mathbb{Z}^4.
$$

More explicitly,

$$
D = I_t\times I_x\times I_y\times I_z,
$$

with unused spatial intervals set to the singleton set $\{0\}$.

For example:

$$
\begin{aligned}
t+0\mathrm{D}:&\quad
D=I_t\times\{0\}\times\{0\}\times\{0\},\\
t+1\mathrm{D}:&\quad
D=I_t\times I_x\times\{0\}\times\{0\},\\
t+2\mathrm{D}:&\quad
D=I_t\times I_x\times I_y\times\{0\},\\
t+3\mathrm{D}:&\quad
D=I_t\times I_x\times I_y\times I_z.
\end{aligned}
$$

---

## SHAPE

`SHAPE` fixes the finite extent of each axis.

The causal coordinate range is

$$
I_t=\{0,1,\dots,T-1\}.
$$

Each spatial axis is either active or unused:

$$
\begin{aligned}
I_x&=\{L_x,L_x+1,\dots,U_x\}
\quad\text{or}\quad \{0\},\\
I_y&=\{L_y,L_y+1,\dots,U_y\}
\quad\text{or}\quad \{0\},\\
I_z&=\{L_z,L_z+1,\dots,U_z\}
\quad\text{or}\quad \{0\}.
\end{aligned}
$$

Thus

$$
\mathrm{SHAPE}=(I_t,I_x,I_y,I_z).
$$

---

## ALPHABET

`ALPHABET` is the set of possible values stored at each coordinate.

Examples include binary states, $k$-color states, bounded integers, or symbolic states.

Formally,

$$
A
$$

is the cell-state alphabet, and every construction state is a map

$$
X^{(k)}:D\to A.
$$

Common choices include:

$$
\begin{aligned}
A&=\{0,1\}
&&\text{binary cellular automata},\\
A&=\{0,1,\dots,K-1\}
&&K\text{-color cellular automata},\\
A&=\mathbb{Z}/M\mathbb{Z}
&&\text{modular scalar dynamics},\\
A&=\Sigma
&&\text{symbolic states}.
\end{aligned}
$$

---

## SEED

`SEED` specifies the initially written portion of the trajectory.

Let

$$
S_0\subseteq D
$$

be the seed support, and let

$$
\mu_{\mathrm{seed}}
$$

be a distribution over assignments on $S_0$.

Let

$$
a_{\mathrm{init}}\in A
$$

be the initial fill value.

Then

$$
X^{(0)}(c)=
\begin{cases}
\xi(c),
& c\in S_0,\\
a_{\mathrm{init}},
& c\notin S_0,
\end{cases}
\qquad
\xi\sim\mu_{\mathrm{seed}}.
$$

Typical seed supports include:

$$
\begin{aligned}
S_0&=\{[0,0,0,0]\}
&&\text{single scalar seed},\\
S_0&=\{[0,x,0,0]:x\in I_x\}
&&\text{initial } t+1\mathrm{D} \text{ state},\\
S_0&=\{[0,x,y,0]:(x,y)\in I_x\times I_y\}
&&\text{initial } t+2\mathrm{D} \text{ state},\\
S_0&=\{[0,x,y,z]:(x,y,z)\in I_x\times I_y\times I_z\}
&&\text{initial } t+3\mathrm{D} \text{ state}.
\end{aligned}
$$

---

## BOUNDARY

`BOUNDARY` defines how reads behave outside `SHAPE`.

Supported values:

```text
BOUNDARY ∈ {FIXED, PERIODIC, REFLECTIVE}
```

The boundary-extended field is

$$
\widetilde{X}^{(k)}:\mathbb{Z}^4\to A.
$$

It is defined by

$$
\widetilde{X}^{(k)}(c)=
\begin{cases}
X^{(k)}(c),
& c\in D,\\
a_{\mathrm{bdry}},
& c\notin D
\ \land
\mathrm{BOUNDARY}=\mathrm{FIXED},\\
X^{(k)}\!\left(\operatorname{wrap}(c)\right),
& c\notin D
\ \land
\mathrm{BOUNDARY}=\mathrm{PERIODIC},\\
X^{(k)}\!\left(\operatorname{reflect}(c)\right),
& c\notin D
\ \land
\mathrm{BOUNDARY}=\mathrm{REFLECTIVE}.
\end{cases}
$$

Here

$$
a_{\mathrm{bdry}}\in A
$$

is the fixed boundary value.

The helpers

$$
\operatorname{wrap}:\mathbb{Z}^4\to D
$$

and

$$
\operatorname{reflect}:\mathbb{Z}^4\to D
$$

act coordinatewise according to the intervals in `SHAPE`.

---

## NEIGHBORHOOD

`NEIGHBORHOOD` is an ordered collection of relative read stencils.

```text
NEIGHBORHOOD = (NEIGHBORHOOD[1], ..., NEIGHBORHOOD[m])
```

Each `NEIGHBORHOOD[j]` defines a finite, ordered relative-offset read interface. The offset coordinate is

$$
\delta=[\Delta t,\Delta x,\Delta y,\Delta z]\in\mathbb{Z}^4.
$$

The offset $\delta$ is interpreted relative to a target coordinate

$$
c=[t,x,y,z].
$$

Thus the queried coordinate is

$$
c+\delta=[t+\Delta t,\ x+\Delta x,\ y+\Delta y,\ z+\Delta z].
$$

`NEIGHBORHOOD` and `FRONTIER` use the same selector/mask utility. They remain semantically distinct: a neighborhood selects **relative offsets to read**, while a frontier selects **absolute coordinates to write**.

### Shared selector/mask utility

A selector is parameterized by a candidate space $Q$ and a context space $C$:

```text
SELECTOR[Q, C]:
    VARIABLE = q ∈ Q
    CONTEXT = C
    FRAME
    UNIVERSE : C → finite subsets of Q
    PREDICATE = (PREDICATE[1], ..., PREDICATE[n])
    COMBINE
    ORDER
```

The fields have the following meanings:

- `VARIABLE` names the candidate being tested.
- `CONTEXT` lists the external values available to the universe generator and predicates.
- `FRAME` records whether the candidate is an absolute coordinate or a relative offset.
- `UNIVERSE` generates the finite candidate set to search.
- `PREDICATE` filters candidate values.
- `COMBINE` combines predicate values into one inclusion decision.
- `ORDER` turns the selected candidates into a canonical sequence when order matters.

For a selector $S=\mathrm{SELECTOR}[Q,C]$, let

$$
\Omega_S(C)\subseteq Q
$$

be the finite candidate set returned by `UNIVERSE` in context $C$. Let

$$
P_1,\dots,P_n:Q\times C\to\{0,1\}
$$

be the selector predicates, and let

$$
\Psi:\{0,1\}^n\to\{0,1\}
$$

be the selector combiner. The selected candidate set is

$$
\operatorname{Select}_S(C)
=
\operatorname{ORDER}\!\left(
\left\{
q\in\Omega_S(C):
\Psi\!\left(P_1(q,C),\dots,P_n(q,C)\right)=1
\right\}
\right).
$$

If `ORDER = NONE`, the selected value is semantically an unordered finite set. If an implementation needs deterministic enumeration for batching, logging, visualization, or reproducible stochastic sampling, it may still use an implementation-level canonical enumeration without changing the mathematical write semantics.

### Selector specialization for neighborhoods

For neighborhoods, the selector is specialized as follows:

```text
NEIGHBORHOOD[j]:
    SELECTOR[Q_N, C_N]
    Q_N = Z⁴
    C_N = (c, k, X̃⁽ᵏ⁾)
    VARIABLE = δ = [Δt, Δx, Δy, Δz]
    FRAME = RELATIVE_TO_TARGET
    UNIVERSE = Ω_j : C_N → finite subsets of Z⁴
    PREDICATE = (η_j,1, ..., η_j,n)
    COMBINE = Ψ_j
    ORDER = ord_j
    READ_MODE ∈ {COMPACT_SELECTED, FIXED_SUPPORT_WITH_MASK}
```

The neighborhood context is

$$
C_N=(c,k,\widetilde{X}^{(k)}).
$$

Each predicate has type

$$
\eta_{j,\ell}:\mathbb{Z}^4\times C_N\to\{0,1\}.
$$

Equivalently,

$$
\eta_{j,\ell}(\delta,c,k,\widetilde{X}^{(k)})\in\{0,1\}.
$$

In the usual static-stencil case, predicates depend only on $\delta$:

$$
\eta_{j,\ell}(\delta)\in\{0,1\}.
$$

The selected offset sequence is

$$
N_j(c,k,\widetilde{X}^{(k)})
=
\operatorname{ord}_j\!\left(
\left\{
\delta\in\Omega_j(c,k,\widetilde{X}^{(k)}):
\Psi_j\!\left(
\eta_{j,1}(\delta,c,k,\widetilde{X}^{(k)}),
\dots,
\eta_{j,n_j}(\delta,c,k,\widetilde{X}^{(k)})
\right)=1
\right\}
\right).
$$

In the static case, this reduces to a fixed ordered offset sequence

$$
N_j
=
\operatorname{ord}_j\!\left(
\left\{
\delta\in\Omega_j:
\Psi_j\!\left(\eta_{j,1}(\delta),\dots,\eta_{j,n_j}(\delta)\right)=1
\right\}
\right).
$$

### Inactive spatial axes

For inactive spatial axes, candidate offsets must be zero. Thus:

```text
t+0D:  Δx = 0, Δy = 0, Δz = 0
t+1D:          Δy = 0, Δz = 0
t+2D:                  Δz = 0
t+3D:  no inactive spatial-axis constraint
```

This constraint may be enforced directly by `UNIVERSE`, by predicates, or by a validation layer. The examples below enforce it through `UNIVERSE`.

### Selector fields

#### `UNIVERSE`

`UNIVERSE` generates the finite candidate set searched by the selector.

For neighborhoods, the natural offset space $\mathbb{Z}^4$ is infinite, so `UNIVERSE` must return a finite candidate set:

$$
\Omega_j(c,k,\widetilde{X}^{(k)})\subset\mathbb{Z}^4.
$$

For static neighborhoods, `UNIVERSE` is usually a fixed finite offset set $\Omega_j$. For example,

```text
UNIVERSE = {[-1, Δx, Δy, 0] : Δx, Δy ∈ {-1,0,1}}
```

considers only offsets on the previous time slice, inside a $3\times3$ spatial window, with the $z$ axis inactive.

#### `PREDICATE`

`PREDICATE` decides whether a candidate offset is included. Predicates may be purely geometric, coordinate-dependent, round-dependent, or state-dependent:

```text
static stencil:                  η(δ)
coordinate-dependent stencil:    η(δ, c)
round-dependent stencil:         η(δ, c, k)
state-dependent adaptive stencil: η(δ, c, k, X̃⁽ᵏ⁾)
```

#### `COMBINE`

`COMBINE` combines multiple predicate outputs into one inclusion decision.

Common choices are:

```text
COMBINE = IDENTITY    if there is one predicate
COMBINE = AND         include only when all predicates are true
COMBINE = OR          include when any predicate is true
```

Arbitrary Boolean formulas may also be used:

```text
(P1 AND P2) OR (P3 AND NOT P4)
```

The default is:

```text
COMBINE = IDENTITY    if there is one predicate
COMBINE = AND         if multiple predicates are listed without another combiner
```

#### `ORDER`

`ORDER` defines the order of the selected offsets.

For neighborhoods, order matters because the rule receives a read vector. The default neighborhood order is lexicographic order over

$$
[\Delta t,\Delta x,\Delta y,\Delta z].
$$

Thus

```text
ORDER = LEX(Δt, Δx, Δy, Δz)
```

is the default unless another order is specified.

### Read modes

A neighborhood can expose its reads in one of two modes:

```text
READ_MODE ∈ {COMPACT_SELECTED, FIXED_SUPPORT_WITH_MASK}
```

#### `READ_MODE = COMPACT_SELECTED`

This is the default. The rule receives only the selected offsets and their values.

Let

$$
N_j(c,k,\widetilde{X}^{(k)})=(\delta_{j,1},\dots,\delta_{j,n}).
$$

The compact read vector is

$$
\mathcal{N}_j(c;\widetilde{X}^{(k)})
=
\left(
\widetilde{X}^{(k)}(c+\delta_{j,1}),
\dots,
\widetilde{X}^{(k)}(c+\delta_{j,n})
\right).
$$

If the selector is dynamic, the length $n$ may vary with $c$, $k$, or $\widetilde{X}^{(k)}$. Variable-length compact reads are most natural for `FORMULAIC`, `STOCHASTIC`, attention-like, or otherwise variable-arity rule implementations.

For lookup-based rule types such as `EXHAUSTIVE`, `ISOTROPIC`, fixed-arity `SEMI-TOTALISTIC`, and fixed-arity `TOTALISTIC` rules, `COMPACT_SELECTED` should use static or otherwise fixed-arity neighborhoods.

#### `READ_MODE = FIXED_SUPPORT_WITH_MASK`

This mode keeps a fixed read shape while allowing adaptive inclusion masks.

Let the neighborhood support be a fixed ordered sequence

$$
\Omega_j=(\omega_{j,1},\dots,\omega_{j,s})\subset\mathbb{Z}^4.
$$

The rule receives both the full support values

$$
V_j(c;\widetilde{X}^{(k)})
=
\left(
\widetilde{X}^{(k)}(c+\omega_{j,1}),
\dots,
\widetilde{X}^{(k)}(c+\omega_{j,s})
\right)
$$

and the inclusion mask

$$
M_j(c,k,\widetilde{X}^{(k)})
=
\left(
\mu_{j,1},
\dots,
\mu_{j,s}
\right),
$$

where

$$
\mu_{j,a}
=
\Psi_j\!\left(
\eta_{j,1}(\omega_{j,a},c,k,\widetilde{X}^{(k)}),
\dots,
\eta_{j,n_j}(\omega_{j,a},c,k,\widetilde{X}^{(k)})
\right).
$$

The selected offsets are those support offsets whose mask entry equals 1. This mode is useful when the selector is adaptive but the rule still needs fixed-shape inputs.

In later `RULE` formulas, $\mathcal{N}_j$ denotes the neighborhood read object produced by the selected `READ_MODE`: either the compact value vector, or the fixed support values together with their mask.

### Boundary interaction

`NEIGHBORHOOD` chooses which offsets to read. `BOUNDARY` determines how reads behave when the queried coordinate lies outside $D$.

When $c+\delta\notin D$, the read is resolved by the boundary-extended field $\widetilde{X}^{(k)}$.

### Timestep-causal convention

For state-autoregressive next-state prediction, neighborhoods should only read from causal context.

If a target coordinate is

$$
c=[t,x,y,z],
$$

then a read offset

$$
\delta=[\Delta t,\Delta x,\Delta y,\Delta z]
$$

is timestep-causal when

$$
\Delta t\le -1.
$$

Thus the target state at schedule coordinate $t$ is predicted only from states with coordinates

$$
t+\Delta t \le t-1.
$$

This implements prediction of state $t$ from states $<t$, or equivalently prediction of state $t+1$ from states $\le t$.

### Predicate macros

The macro layer includes `RADIUS`, `METRIC`, `REGION`, `FOV`, and axis-scoped `CHANGE_COUNT`. These are reusable predicate macros rather than primitive neighborhood fields.

The previous implicit four-dimensional change-count concept is replaced by axis-scoped `CHANGE_COUNT`.

A predicate macro is only syntax. It expands to an ordinary selector predicate and does not change the selector semantics.

#### Axis-scoped projection

For a set of axes

$$
B\subseteq\{t,x,y,z\},
$$

write $\delta_B$ for the projection of $\delta$ onto those axes.

For example, if $B=\{x,y\}$, then

$$
\delta_B=(\Delta x,\Delta y).
$$

#### `METRIC_NORM`

The metric macro maps to norms over a chosen axis set $B$:

$$
\|\delta_B\|_1
=
\sum_{a\in B}|\Delta a|,
$$

$$
\|\delta_B\|_2
=
\sqrt{\sum_{a\in B}(\Delta a)^2},
$$

and

$$
\|\delta_B\|_\infty
=
\max_{a\in B}|\Delta a|.
$$

#### `RADIUS`

A filled radius macro expands to

```text
RADIUS(axes=B, METRIC=L1, REGION=FILLED, r)
```

meaning

$$
\|\delta_B\|_1\le r.
$$

With `METRIC = L2`, use $\|\delta_B\|_2\le r$. With `METRIC = LINF`, use $\|\delta_B\|_\infty\le r$.

A shell radius macro expands to

```text
RADIUS(axes=B, METRIC=L1, REGION=SHELL, r)
```

meaning

$$
\|\delta_B\|_1 = r.
$$

Again, `METRIC = L2` and `METRIC = LINF` use the corresponding norm.

#### `CHANGE_COUNT`

The axis-scoped change count is

$$
\operatorname{change}_B(\delta)
=
\sum_{a\in B}\mathbf{1}[\Delta a\ne 0].
$$

The predicate macro

```text
CHANGE_COUNT(axes=B, K=K_set)
```

means

$$
\operatorname{change}_B(\delta)\in K_{\mathrm{set}}.
$$

Examples:

```text
CHANGE_COUNT(axes={x,y}, K={1})
```

selects offsets where exactly one of the spatial axes $x,y$ changes.

```text
CHANGE_COUNT(axes={x,y,z}, K={3})
```

selects 3D corner-like offsets where all three spatial axes change.

Because the axes are explicit, temporal lag such as $\Delta t=-1$ does not accidentally affect spatial change-count predicates.

#### `FOV`

A directional field-of-view macro may be used as a predicate. Given a reference offset $\rho$, unit vector $u$, and aperture $\theta$:

$$
\eta_{\mathrm{FOV}}(\delta)=
\begin{cases}
1,
& \delta=\rho,\\
\mathbf{1}\!\left[
\dfrac{(\delta-\rho)\cdot u}{|\delta-\rho|_2}
\ge
\cos\!\left(\dfrac{\theta}{2}\right)
\right],
& \delta\ne\rho.
\end{cases}
$$

The first case avoids division by zero at the reference offset.

#### Other common macros

Useful derived predicates include:

```text
TEMPORAL_LAG(h):        Δt = h
ZERO_AXES(B):           Δa = 0 for every a ∈ B
NONZERO(axes=B):        exists a ∈ B such that Δa ≠ 0
PREVIOUS_SPATIAL_CENTER: Δt = -1 and Δx = Δy = Δz = 0 on active spatial axes
```

For formal semantics, Euclidean predicates use the exact lattice set induced by $\|\delta_B\|_2$. For visualization or rasterized mask generation, an implementation may use supersampling. This visualization convention does not change the formal neighborhood definition.

### Coordinate convention for examples

The examples below use

```text
c = [t, x, y, z]
δ = [Δt, Δx, Δy, Δz]
```

with the following spatial orientation conventions:

```text
2D:
+x = right / east
+y = up / north

3D:
+x = right / east
+y = forward / north
+z = up / altitude
```

This is a right-handed Cartesian coordinate system with ENU / `z`-up convention.

For the directional labels used in the 2D examples below:

```text
N = Δy = +1
S = Δy = -1
W = Δx = -1
E = Δx = +1
```

The examples assume state-autoregressive next-state prediction, so neighborhoods read from the previous time slice:

```text
Δt = -1
```

For same-slice spatial masks, change `Δt = -1` to `Δt = 0`.

### Example: Moore neighborhood in 2D

The proper 2D Moore neighborhood is the eight surrounding cells on the previous time slice.

```text
NEIGHBORHOOD Moore2D:
    SELECTOR[Q_N, C_N]
    Q_N = Z⁴
    C_N = (c, k, X̃⁽ᵏ⁾)
    VARIABLE = δ
    FRAME = RELATIVE_TO_TARGET

    UNIVERSE =
        {[-1, Δx, Δy, 0] :
            Δx ∈ {-1,0,1},
            Δy ∈ {-1,0,1}}

    PREDICATE[1](δ) =
        RADIUS(axes={x,y}, METRIC=LINF, REGION=FILLED, r=1)

    PREDICATE[2](δ) =
        NONZERO(axes={x,y})

    COMBINE = AND
    ORDER = LEX(Δt, Δx, Δy, Δz)
    READ_MODE = COMPACT_SELECTED
```

Selected offsets:

```text
[-1,-1,-1,0]   SW
[-1,-1, 0,0]   W
[-1,-1, 1,0]   NW
[-1, 0,-1,0]   S
[-1, 0, 1,0]   N
[-1, 1,-1,0]   SE
[-1, 1, 0,0]   E
[-1, 1, 1,0]   NE
```

For the nine-cell previous-slice spatial stencil, including the previous spatial center `[-1,0,0,0]`, remove `PREDICATE[2]`.

### Example: Moore neighborhood in 3D

The proper 3D Moore neighborhood is the 26 surrounding voxels on the previous time slice of a $3\times3\times3$ cube.

```text
NEIGHBORHOOD Moore3D:
    SELECTOR[Q_N, C_N]
    Q_N = Z⁴
    C_N = (c, k, X̃⁽ᵏ⁾)
    VARIABLE = δ
    FRAME = RELATIVE_TO_TARGET

    UNIVERSE =
        {[-1, Δx, Δy, Δz] :
            Δx ∈ {-1,0,1},
            Δy ∈ {-1,0,1},
            Δz ∈ {-1,0,1}}

    PREDICATE[1](δ) =
        RADIUS(axes={x,y,z}, METRIC=LINF, REGION=FILLED, r=1)

    PREDICATE[2](δ) =
        NONZERO(axes={x,y,z})

    COMBINE = AND
    ORDER = LEX(Δt, Δx, Δy, Δz)
    READ_MODE = COMPACT_SELECTED
```

Selected count:

```text
26 offsets
```

For the 27-cell previous-slice spatial stencil, including the previous spatial center `[-1,0,0,0]`, remove `PREDICATE[2]`.

### Example: Von Neumann neighborhood in 2D

The proper 2D Von Neumann neighborhood is the four cardinal cells on the previous time slice.

```text
NEIGHBORHOOD VonNeumann2D:
    SELECTOR[Q_N, C_N]
    Q_N = Z⁴
    C_N = (c, k, X̃⁽ᵏ⁾)
    VARIABLE = δ
    FRAME = RELATIVE_TO_TARGET

    UNIVERSE =
        {[-1, Δx, Δy, 0] :
            Δx ∈ {-1,0,1},
            Δy ∈ {-1,0,1}}

    PREDICATE[1](δ) =
        RADIUS(axes={x,y}, METRIC=L1, REGION=SHELL, r=1)

    COMBINE = IDENTITY
    ORDER = LEX(Δt, Δx, Δy, Δz)
    READ_MODE = COMPACT_SELECTED
```

Selected offsets:

```text
[-1,-1, 0,0]   W
[-1, 0,-1,0]   S
[-1, 0, 1,0]   N
[-1, 1, 0,0]   E
```

For the five-cell previous-slice cross, including the previous spatial center, use

```text
RADIUS(axes={x,y}, METRIC=L1, REGION=FILLED, r=1)
```

instead of

```text
RADIUS(axes={x,y}, METRIC=L1, REGION=SHELL, r=1)
```

### Example: Von Neumann neighborhood in 3D

The proper 3D Von Neumann neighborhood is the six axis-adjacent voxels on the previous time slice.

```text
NEIGHBORHOOD VonNeumann3D:
    SELECTOR[Q_N, C_N]
    Q_N = Z⁴
    C_N = (c, k, X̃⁽ᵏ⁾)
    VARIABLE = δ
    FRAME = RELATIVE_TO_TARGET

    UNIVERSE =
        {[-1, Δx, Δy, Δz] :
            Δx ∈ {-1,0,1},
            Δy ∈ {-1,0,1},
            Δz ∈ {-1,0,1}}

    PREDICATE[1](δ) =
        RADIUS(axes={x,y,z}, METRIC=L1, REGION=SHELL, r=1)

    COMBINE = IDENTITY
    ORDER = LEX(Δt, Δx, Δy, Δz)
    READ_MODE = COMPACT_SELECTED
```

Selected count:

```text
6 offsets
```

For the seven-cell previous-slice cross, including the previous spatial center, use

```text
RADIUS(axes={x,y,z}, METRIC=L1, REGION=FILLED, r=1)
```

### Example: NW, N, and NE above a cell in 2D

This reads the three cells directly above the target cell, i.e. one unit in `+y` / north, on the previous time slice:

```text
NW, N, NE
```

Relative to target $[t,x,y,0]$, these are:

```text
[t-1, x-1, y+1, 0]
[t-1, x,   y+1, 0]
[t-1, x+1, y+1, 0]
```

As offsets:

```text
[-1,-1, 1,0]
[-1, 0, 1,0]
[-1, 1, 1,0]
```

Selector:

```text
NEIGHBORHOOD NorthTriple2D:
    SELECTOR[Q_N, C_N]
    Q_N = Z⁴
    C_N = (c, k, X̃⁽ᵏ⁾)
    VARIABLE = δ
    FRAME = RELATIVE_TO_TARGET

    UNIVERSE =
        {[-1, Δx, Δy, 0] :
            Δx ∈ {-1,0,1},
            Δy ∈ {1}}

    PREDICATE[1](δ) = true

    COMBINE = IDENTITY
    ORDER = LEX(Δt, Δx, Δy, Δz)
    READ_MODE = COMPACT_SELECTED
```

Equivalent predicate-style version:

```text
NEIGHBORHOOD NorthTriple2D:
    SELECTOR[Q_N, C_N]
    Q_N = Z⁴
    C_N = (c, k, X̃⁽ᵏ⁾)
    VARIABLE = δ
    FRAME = RELATIVE_TO_TARGET

    UNIVERSE =
        {[-1, Δx, Δy, 0] :
            Δx ∈ {-1,0,1},
            Δy ∈ {-1,0,1}}

    PREDICATE[1](δ) =
        Δy = 1

    PREDICATE[2](δ) =
        RADIUS(axes={x}, METRIC=LINF, REGION=FILLED, r=1)

    COMBINE = AND
    ORDER = LEX(Δt, Δx, Δy, Δz)
    READ_MODE = COMPACT_SELECTED
```

### Example: NW, N, and NE offset north by one row

This reads the same horizontal triple one row farther north on the previous time slice:

```text
[t-1, x-1, y+2, 0]
[t-1, x,   y+2, 0]
[t-1, x+1, y+2, 0]
```

As offsets:

```text
[-1,-1, 2,0]
[-1, 0, 2,0]
[-1, 1, 2,0]
```

Selector:

```text
NEIGHBORHOOD NorthTriple2D_OffsetNorth1:
    SELECTOR[Q_N, C_N]
    Q_N = Z⁴
    C_N = (c, k, X̃⁽ᵏ⁾)
    VARIABLE = δ
    FRAME = RELATIVE_TO_TARGET

    UNIVERSE =
        {[-1, Δx, Δy, 0] :
            Δx ∈ {-1,0,1},
            Δy ∈ {2}}

    PREDICATE[1](δ) = true

    COMBINE = IDENTITY
    ORDER = LEX(Δt, Δx, Δy, Δz)
    READ_MODE = COMPACT_SELECTED
```

Predicate-style version:

```text
NEIGHBORHOOD NorthTriple2D_OffsetNorth1:
    SELECTOR[Q_N, C_N]
    Q_N = Z⁴
    C_N = (c, k, X̃⁽ᵏ⁾)
    VARIABLE = δ
    FRAME = RELATIVE_TO_TARGET

    UNIVERSE =
        {[-1, Δx, Δy, 0] :
            Δx ∈ {-1,0,1},
            Δy ∈ {-1,0,1,2}}

    PREDICATE[1](δ) =
        Δy = 2

    PREDICATE[2](δ) =
        RADIUS(axes={x}, METRIC=LINF, REGION=FILLED, r=1)

    COMBINE = AND
    ORDER = LEX(Δt, Δx, Δy, Δz)
    READ_MODE = COMPACT_SELECTED
```

### Example: Only corners in 2D

For a 2D $3\times3$ previous-slice spatial window, the corners are:

```text
[-1,-1,-1,0]   SW
[-1,-1, 1,0]   NW
[-1, 1,-1,0]   SE
[-1, 1, 1,0]   NE
```

Selector:

```text
NEIGHBORHOOD Corners2D:
    SELECTOR[Q_N, C_N]
    Q_N = Z⁴
    C_N = (c, k, X̃⁽ᵏ⁾)
    VARIABLE = δ
    FRAME = RELATIVE_TO_TARGET

    UNIVERSE =
        {[-1, Δx, Δy, 0] :
            Δx ∈ {-1,0,1},
            Δy ∈ {-1,0,1}}

    PREDICATE[1](δ) =
        CHANGE_COUNT(axes={x,y}, K={2})

    COMBINE = IDENTITY
    ORDER = LEX(Δt, Δx, Δy, Δz)
    READ_MODE = COMPACT_SELECTED
```

Selected count:

```text
4 offsets
```

### Example: Only corners in 3D

For a 3D $3\times3\times3$ previous-slice spatial cube, the corners are the eight offsets where every spatial coordinate changes by one:

```text
Δx ∈ {-1,1}
Δy ∈ {-1,1}
Δz ∈ {-1,1}
```

Selector:

```text
NEIGHBORHOOD Corners3D:
    SELECTOR[Q_N, C_N]
    Q_N = Z⁴
    C_N = (c, k, X̃⁽ᵏ⁾)
    VARIABLE = δ
    FRAME = RELATIVE_TO_TARGET

    UNIVERSE =
        {[-1, Δx, Δy, Δz] :
            Δx ∈ {-1,0,1},
            Δy ∈ {-1,0,1},
            Δz ∈ {-1,0,1}}

    PREDICATE[1](δ) =
        CHANGE_COUNT(axes={x,y,z}, K={3})

    COMBINE = IDENTITY
    ORDER = LEX(Δt, Δx, Δy, Δz)
    READ_MODE = COMPACT_SELECTED
```

Selected count:

```text
8 offsets
```

### Example: Previous self only

Useful when the target cell's previous state should be separated from its surrounding neighbors.

```text
NEIGHBORHOOD PreviousSelf:
    SELECTOR[Q_N, C_N]
    Q_N = Z⁴
    C_N = (c, k, X̃⁽ᵏ⁾)
    VARIABLE = δ
    FRAME = RELATIVE_TO_TARGET

    UNIVERSE = {[-1,0,0,0]}

    PREDICATE[1](δ) = true

    COMBINE = IDENTITY
    ORDER = LEX(Δt, Δx, Δy, Δz)
    READ_MODE = COMPACT_SELECTED
```

A Life-like rule can then use:

```text
NEIGHBORHOOD[1] = PreviousSelf
NEIGHBORHOOD[2] = Moore2D
```

instead of using a single previous-slice spatial stencil that includes the previous spatial center.

### Example: Radius-r Moore neighborhood in 2D

```text
NEIGHBORHOOD Moore2D_RadiusR:
    SELECTOR[Q_N, C_N]
    Q_N = Z⁴
    C_N = (c, k, X̃⁽ᵏ⁾)
    VARIABLE = δ
    FRAME = RELATIVE_TO_TARGET

    UNIVERSE =
        {[-1, Δx, Δy, 0] :
            Δx ∈ {-r, ..., r},
            Δy ∈ {-r, ..., r}}

    PREDICATE[1](δ) =
        RADIUS(axes={x,y}, METRIC=LINF, REGION=FILLED, r)

    PREDICATE[2](δ) =
        NONZERO(axes={x,y})

    COMBINE = AND
    ORDER = LEX(Δt, Δx, Δy, Δz)
    READ_MODE = COMPACT_SELECTED
```

### Example: Radius-r Von Neumann neighborhood in 2D

Filled diamond:

```text
NEIGHBORHOOD VonNeumann2D_FilledRadiusR:
    SELECTOR[Q_N, C_N]
    Q_N = Z⁴
    C_N = (c, k, X̃⁽ᵏ⁾)
    VARIABLE = δ
    FRAME = RELATIVE_TO_TARGET

    UNIVERSE =
        {[-1, Δx, Δy, 0] :
            Δx ∈ {-r, ..., r},
            Δy ∈ {-r, ..., r}}

    PREDICATE[1](δ) =
        RADIUS(axes={x,y}, METRIC=L1, REGION=FILLED, r)

    PREDICATE[2](δ) =
        NONZERO(axes={x,y})

    COMBINE = AND
    ORDER = LEX(Δt, Δx, Δy, Δz)
    READ_MODE = COMPACT_SELECTED
```

Shell only:

```text
NEIGHBORHOOD VonNeumann2D_ShellRadiusR:
    SELECTOR[Q_N, C_N]
    Q_N = Z⁴
    C_N = (c, k, X̃⁽ᵏ⁾)
    VARIABLE = δ
    FRAME = RELATIVE_TO_TARGET

    UNIVERSE =
        {[-1, Δx, Δy, 0] :
            Δx ∈ {-r, ..., r},
            Δy ∈ {-r, ..., r}}

    PREDICATE[1](δ) =
        RADIUS(axes={x,y}, METRIC=L1, REGION=SHELL, r)

    COMBINE = IDENTITY
    ORDER = LEX(Δt, Δx, Δy, Δz)
    READ_MODE = COMPACT_SELECTED
```

---

## FRONTIER

`FRONTIER` is an ordered collection of absolute-coordinate write selectors.

```text
FRONTIER = (FRONTIER[1], ..., FRONTIER[q])
```

Each `FRONTIER[i]` selects actual writable coordinates

$$
c=[t,x,y,z]\in D
$$

from the persistent trajectory domain. Unlike neighborhoods, frontiers select absolute coordinates, not relative offsets.

### Selector specialization for frontiers

For frontiers, the shared selector is specialized as follows:

```text
FRONTIER[i]:
    SELECTOR[Q_F, C_F]
    Q_F = D
    C_F = (k, X̃⁽ᵏ⁾)
    VARIABLE = c = [t, x, y, z]
    FRAME = ABSOLUTE
    UNIVERSE = U_i : C_F → finite subsets of D
    PREDICATE = (φ_i,1, ..., φ_i,n)
    COMBINE = Φ_i
    ORDER = ord_i
```

The frontier context is

$$
C_F=(k,\widetilde{X}^{(k)}).
$$

Each predicate has type

$$
\phi_{i,\ell}:D\times C_F\to\{0,1\}.
$$

Equivalently,

$$
\phi_{i,\ell}(c,k,\widetilde{X}^{(k)})\in\{0,1\}.
$$

If a frontier predicate is purely geometric, it may ignore $\widetilde{X}^{(k)}$.

The component write set is

$$
F_{i,k}
=
\left\{
c\in U_i(k,\widetilde{X}^{(k)}):
\Phi_i\!\left(
\phi_{i,1}(c,k,\widetilde{X}^{(k)}),
\dots,
\phi_{i,n_i}(c,k,\widetilde{X}^{(k)})
\right)=1
\right\}.
$$

A top-level Boolean combiner

$$
\Phi_{\mathrm{frontier}}:\{0,1\}^q\to\{0,1\}
$$

combines the component frontiers into the active frontier predicate:

$$
\phi(c,k,\widetilde{X}^{(k)})
=
\Phi_{\mathrm{frontier}}\!\left(
\mathbf{1}[c\in F_{1,k}],
\dots,
\mathbf{1}[c\in F_{q,k}]
\right).
$$

The active write set at construction round $k$ is

$$
F_k
=
\{c\in D:\phi(c,k,\widetilde{X}^{(k)})=1\}.
$$

All coordinates in $F_k$ are updated in parallel from the same old snapshot $\widetilde{X}^{(k)}$.

### Defaults

```text
UNIVERSE = D
COMBINE = IDENTITY        if there is one predicate
COMBINE = AND             if multiple predicates are listed without another combiner
ORDER = NONE
FRONTIER_COMBINE = OR
```

Inside one frontier selector, `COMBINE` combines that selector's predicates. Across multiple frontier components, `FRONTIER_COMBINE` combines the component write sets.

Equivalently, for multiple frontier components,

$$
\Phi_{\mathrm{frontier}}(b_1,\dots,b_q)=b_1\lor\cdots\lor b_q.
$$

If $q=1$, then

$$
\Phi_{\mathrm{frontier}}(b_1)=b_1.
$$

`ORDER = NONE` means frontier order has no mathematical effect because writes are parallel. An implementation may still use a deterministic enumeration such as lexicographic order for batching, logging, visualization, or reproducible stochastic sampling.

### Example: Full next-state slice

This is the standard CA update schedule.

```text
FRONTIER FullNextSlice:
    SELECTOR[Q_F, C_F]
    Q_F = D
    C_F = (k, X̃⁽ᵏ⁾)
    VARIABLE = c
    FRAME = ABSOLUTE

    UNIVERSE = D

    PREDICATE[1](c,k,X̃) =
        t = k + 1

    COMBINE = IDENTITY
    ORDER = NONE
```

At construction round $k$, this writes

$$
F_k=\{[k+1,x,y,z]\in D\}.
$$

### Example: Current construction slice

This writes the slice whose explicit time coordinate equals $k$.

```text
FRONTIER CurrentSlice:
    SELECTOR[Q_F, C_F]
    Q_F = D
    C_F = (k, X̃⁽ᵏ⁾)
    VARIABLE = c
    FRAME = ABSOLUTE

    UNIVERSE = D

    PREDICATE[1](c,k,X̃) =
        t = k

    COMBINE = IDENTITY
    ORDER = NONE
```

This is useful when the seed is not necessarily locked to $t=0$, or when construction round and time coordinate are intentionally aligned.

### Example: Skipped slices

```text
FRONTIER SkippedSlices:
    SELECTOR[Q_F, C_F]
    Q_F = D
    C_F = (k, X̃⁽ᵏ⁾)
    VARIABLE = c
    FRAME = ABSOLUTE

    UNIVERSE = D

    PREDICATE[1](c,k,X̃) =
        t = 2k

    COMBINE = IDENTITY
    ORDER = NONE
```

### Example: Even/odd schedule class

```text
FRONTIER EvenOddScheduleClass:
    SELECTOR[Q_F, C_F]
    Q_F = D
    C_F = (k, X̃⁽ᵏ⁾)
    VARIABLE = c
    FRAME = ABSOLUTE

    UNIVERSE = D

    PREDICATE[1](c,k,X̃) =
        t mod 2 = k mod 2

    COMBINE = IDENTITY
    ORDER = NONE
```

### Example: Single row in a 2D slice

This writes only row $y=y_0$ of the next slice.

```text
FRONTIER SingleRow2D:
    SELECTOR[Q_F, C_F]
    Q_F = D
    C_F = (k, X̃⁽ᵏ⁾)
    VARIABLE = c
    FRAME = ABSOLUTE

    UNIVERSE = D

    PREDICATE[1](c,k,X̃) =
        t = k + 1

    PREDICATE[2](c,k,X̃) =
        y = y₀

    COMBINE = AND
    ORDER = NONE
```

The write set is

$$
F_k=\{[k+1,x,y_0,0]\in D\}.
$$

### Example: Moving row in 2D

This writes row $y=k$ of slice $t=k+1$.

```text
FRONTIER MovingRow2D:
    SELECTOR[Q_F, C_F]
    Q_F = D
    C_F = (k, X̃⁽ᵏ⁾)
    VARIABLE = c
    FRAME = ABSOLUTE

    UNIVERSE = D

    PREDICATE[1](c,k,X̃) =
        t = k + 1

    PREDICATE[2](c,k,X̃) =
        y = k

    COMBINE = AND
    ORDER = NONE
```

A bounded or wrapping version is:

```text
PREDICATE[2](c,k,X̃) =
    y = L_y + (k mod |I_y|)
```

This gives a repeating row sweep.

### Example: Plane in 3D

```text
FRONTIER Plane3D:
    SELECTOR[Q_F, C_F]
    Q_F = D
    C_F = (k, X̃⁽ᵏ⁾)
    VARIABLE = c
    FRAME = ABSOLUTE

    UNIVERSE = D

    PREDICATE[1](c,k,X̃) =
        t = k + 1

    PREDICATE[2](c,k,X̃) =
        z = z₀

    COMBINE = AND
    ORDER = NONE
```

### Example: Main diagonal in 2D

```text
FRONTIER MainDiagonal2D:
    SELECTOR[Q_F, C_F]
    Q_F = D
    C_F = (k, X̃⁽ᵏ⁾)
    VARIABLE = c
    FRAME = ABSOLUTE

    UNIVERSE = D

    PREDICATE[1](c,k,X̃) =
        t = k + 1

    PREDICATE[2](c,k,X̃) =
        x = y

    COMBINE = AND
    ORDER = NONE
```

### Example: Anti-diagonal in 2D

```text
FRONTIER AntiDiagonal2D:
    SELECTOR[Q_F, C_F]
    Q_F = D
    C_F = (k, X̃⁽ᵏ⁾)
    VARIABLE = c
    FRAME = ABSOLUTE

    UNIVERSE = D

    PREDICATE[1](c,k,X̃) =
        t = k + 1

    PREDICATE[2](c,k,X̃) =
        x + y = b

    COMBINE = AND
    ORDER = NONE
```

### Example: Checkerboard sublattice in the next slice

This writes alternating spatial cells.

```text
FRONTIER Checkerboard2D:
    SELECTOR[Q_F, C_F]
    Q_F = D
    C_F = (k, X̃⁽ᵏ⁾)
    VARIABLE = c
    FRAME = ABSOLUTE

    UNIVERSE = D

    PREDICATE[1](c,k,X̃) =
        t = k + 1

    PREDICATE[2](c,k,X̃) =
        (x + y) mod 2 = 0

    COMBINE = AND
    ORDER = NONE
```

The complementary checkerboard is:

```text
(x + y) mod 2 = 1
```

Alternating checkerboards by construction round can be written as:

```text
PREDICATE[2](c,k,X̃) =
    (x + y) mod 2 = k mod 2
```

### Example: Manhattan shell in 2D

```text
FRONTIER ManhattanShell2D:
    SELECTOR[Q_F, C_F]
    Q_F = D
    C_F = (k, X̃⁽ᵏ⁾)
    VARIABLE = c
    FRAME = ABSOLUTE

    UNIVERSE = D

    PREDICATE[1](c,k,X̃) =
        t = k + 1

    PREDICATE[2](c,k,X̃) =
        |x - x₀| + |y - y₀| = r

    COMBINE = AND
    ORDER = NONE
```

### Example: Ring-by-ring growth in 2D

```text
FRONTIER ManhattanRingGrowth2D:
    SELECTOR[Q_F, C_F]
    Q_F = D
    C_F = (k, X̃⁽ᵏ⁾)
    VARIABLE = c
    FRAME = ABSOLUTE

    UNIVERSE = D

    PREDICATE[1](c,k,X̃) =
        t = t₀

    PREDICATE[2](c,k,X̃) =
        |x - x₀| + |y - y₀| = k

    COMBINE = AND
    ORDER = NONE
```

This writes a growing diamond-shaped shell within one time slice.

For a filled growing diamond, use:

```text
|x - x₀| + |y - y₀| ≤ k
```

### Example: State-dependent active frontier for next-state generation

This writes next-slice coordinates adjacent to active cells in the previous time slice.

```text
FRONTIER ActiveWavefront2D:
    SELECTOR[Q_F, C_F]
    Q_F = D
    C_F = (k, X̃⁽ᵏ⁾)
    VARIABLE = c
    FRAME = ABSOLUTE

    UNIVERSE = D

    PREDICATE[1](c,k,X̃) =
        t = k + 1

    PREDICATE[2](c,k,X̃) =
        exists δ ∈ AdjacentPrevious2D :
            X̃(c + δ) = a_active

    COMBINE = AND
    ORDER = NONE
```

where

```text
AdjacentPrevious2D =
    { [-1,-1,0,0],
      [-1, 1,0,0],
      [-1,0,-1,0],
      [-1,0, 1,0] }
```

For a candidate coordinate

```text
c = [k+1, x, y, 0]
```

these offsets read

```text
[k, x-1, y,   0]
[k, x+1, y,   0]
[k, x,   y-1, 0]
[k, x,   y+1, 0]
```

This is a true wavefront frontier: the writable next-slice region depends on the already generated previous slice.

For same-slice wavefront construction, use same-slice adjacency offsets with $\Delta t=0$ and a frontier time predicate such as $t=t_0$ rather than $t=k+1$.

---

## RULE

`RULE` maps neighborhood reads to a new value for each coordinate in the active frontier.

All rule types are filtered by `NEIGHBORHOOD`. They differ only in how the local input is represented before the output is selected.

The generator update is

$$
X^{(k+1)}(c)=
\begin{cases}
R\!\left(
c,
k,
\widetilde{X}^{(k)},
\mathcal{N}_1(c;\widetilde{X}^{(k)}),
\dots,
\mathcal{N}_m(c;\widetilde{X}^{(k)})
\right),
& c\in F_k,\\
X^{(k)}(c),
& c\notin F_k.
\end{cases}
$$

All coordinates in $F_k$ are updated in parallel from the same old snapshot $\widetilde{X}^{(k)}$.

---

## RULETYPE = EXHAUSTIVE

`EXHAUSTIVE` is a lookup table over the full ordered local pattern.

Let

$$
\mathcal{N}(c;\widetilde{X}^{(k)})
=
\left(
\mathcal{N}_1(c;\widetilde{X}^{(k)}),
\dots,
\mathcal{N}_m(c;\widetilde{X}^{(k)})
\right).
$$

An exhaustive rule is

$$
R(c,k,\widetilde{X}^{(k)},\mathcal{N})
=T(\mathcal{N}),
$$

where

$$
T:
A^{|N_1|}
\times
\cdots
\times
A^{|N_m|}
\to
A.
$$

---

## RULETYPE = ISOTROPIC

`ISOTROPIC` collapses the exhaustive lookup table by a chosen symmetry group.

For each neighborhood $N_j$, let

$$
G_j
$$

be the selected symmetry group acting on ordered patterns over $N_j$.

The orbit of the local read vector is

$$
[\mathcal{N}_j]_{G_j}
=
\{
g\cdot \mathcal{N}_j:
g\in G_j
\}.
$$

An isotropic rule is

$$
R(c,k,\widetilde{X}^{(k)},\mathcal{N})
=
\widehat{T}\!\left(
[\mathcal{N}_1]_{G_1},
\dots,
[\mathcal{N}_m]_{G_m}
\right).
$$

---

## RULETYPE = SEMI-TOTALISTIC

`SEMI-TOTALISTIC` collapses part of the neighborhood pattern to permutation-invariant aggregates while retaining selected cell states explicitly.

For each neighborhood $N_j$, choose a designated subset

$$
S_j\subseteq N_j
$$

and let

$$
B_j=N_j\setminus S_j.
$$

Let

$$
\Pi_j:A^{|N_j|}\to A^{|S_j|}
$$

be the ordered projection onto the designated cells, and choose an aggregate

$$
\Gamma_j:A^{|B_j|}\to Z_j
$$

for the remaining cells.

The semi-totalistic summary is

$$
\Sigma(\mathcal{N})
=
\left(
\Pi_1(\mathcal{N}_1),
\Gamma_1(\mathcal{N}_1|_{B_1}),
\dots,
\Pi_m(\mathcal{N}_m),
\Gamma_m(\mathcal{N}_m|_{B_m})
\right).
$$

A semi-totalistic rule is

$$
R(c,k,\widetilde{X}^{(k)},\mathcal{N})
=
T\!\left(
\Pi_1(\mathcal{N}_1),
\Gamma_1(\mathcal{N}_1|_{B_1}),
\dots,
\Pi_m(\mathcal{N}_m),
\Gamma_m(\mathcal{N}_m|_{B_m})
\right).
$$

where

$$
T:
A^{|S_1|}
\times
Z_1
\times
\cdots
\times
A^{|S_m|}
\times
Z_m
\to
A.
$$

A common binary case keeps the center state explicit and aggregates the surrounding cells by active count. For a single neighborhood $N$, let $S=\{s\}$ be a singleton designated subset corresponding to the previous-state self entry, and let $B=N\setminus S$. Then

$$
R(c,k,\widetilde{X}^{(k)},\mathcal{N})
=
T\!\left(
\mathcal{N}_{s},
\sum_{\ell\in B}
\mathbf{1}
\!\left[
\mathcal{N}_{\ell}=1
\right]
\right).
$$

If $s$ is the previous-state self entry, then $\mathcal{N}_{s}=\widetilde{X}^{(k)}(c)$. This is the usual outer-totalistic form: the rule depends on the center state and on a totalistic summary of the outer neighborhood.

---

## RULETYPE = TOTALISTIC

`TOTALISTIC` collapses the neighborhood pattern to permutation-invariant aggregates, such as active counts, color histograms, or numeric sums.

For each neighborhood $N_j$, choose an aggregate

$$
\Gamma_j:A^{|N_j|}\to Z_j.
$$

The totalistic summary is

$$
\Gamma(\mathcal{N})
=
\left(
\Gamma_1(\mathcal{N}_1),
\dots,
\Gamma_m(\mathcal{N}_m)
\right).
$$

A totalistic rule is

$$
R(c,k,\widetilde{X}^{(k)},\mathcal{N})
=
T\!\left(
\Gamma_1(\mathcal{N}_1),
\dots,
\Gamma_m(\mathcal{N}_m)
\right).
$$

For binary states, a common aggregate is the active count

$$
\Gamma_j(\mathcal{N}_j)
=
\sum_{\ell=1}^{|N_j|}
\mathbf{1}
\!\left[
\mathcal{N}_{j,\ell}=1
\right].
$$

For $K$-color states, a common aggregate is the color histogram

$$
\Gamma_j(\mathcal{N}_j)
=
\left(
h_{j,0},
\dots,
h_{j,K-1}
\right),
$$

where

$$
h_{j,a}
=
\sum_{\ell=1}^{|N_j|}
\mathbf{1}
\!\left[
\mathcal{N}_{j,\ell}=a
\right].
$$

---

## RULETYPE = FORMULAIC

`FORMULAIC` replaces the lookup table with a deterministic expression that defines the output for every possible input.

A formulaic rule is

$$
R(c,k,\widetilde{X}^{(k)},\mathcal{N})
=
f\!\left(
c,
k,
\widetilde{X}^{(k)},
\mathcal{N}_1,
\dots,
\mathcal{N}_m
\right),
$$

where

$$
f:
D
\times
\mathbb{N}
\times
A^D
\times
A^{|N_1|}
\times
\cdots
\times
A^{|N_m|}
\to
A
$$

is deterministic.

---

## RULETYPE = STOCHASTIC

`STOCHASTIC` defines a probability distribution over outputs and samples from that distribution.

A stochastic rule is

$$
R(c,k,\widetilde{X}^{(k)},\mathcal{N})
\sim
P\!\left(
\cdot
\mid
c,
k,
\widetilde{X}^{(k)},
\mathcal{N}_1,
\dots,
\mathcal{N}_m
\right).
$$

Equivalently,

$$
P:
D
\times
\mathbb{N}
\times
A^D
\times
A^{|N_1|}
\times
\cdots
\times
A^{|N_m|}
\to
\Delta(A),
$$

where

$$
\Delta(A)
$$

is the simplex of probability distributions over $A$.

A stochastic rule may still use exhaustive, isotropic, or totalistic sufficient statistics as its input representation. Its defining feature is that the output is sampled rather than deterministically selected.

---

## State-autoregressive next-state convention

The default trajectory-generation setting stores the full state at every causal coordinate $t$.

For next-state prediction, `FRONTIER` typically selects the next full state slice:

$$
F_k
=
\{
[t,x,y,z]\in D:
t=k+1
\}.
$$

The rule reads from timestep-causal neighborhoods satisfying

$$
\Delta t\le -1.
$$

Thus the model target at coordinate $t=k+1$ is generated from context at coordinates

$$
t\le k.
$$

This implements state-autoregressive next-state prediction:

$$
X_{k+1}=\mathcal{R}(X_{\le k}),
$$

rather than enforcing causality purely through a flat token order.

---

## Complete generator object

A generator instance is fully specified by

$$
\mathcal{G}
=
\left(
D,
A,
S_0,
\mathrm{BOUNDARY},
(N_1,\dots,N_m),
\phi,
R
\right).
$$

Its construction semantics are:

$$
\begin{aligned}
&\text{1. Allocate }D\subseteq\mathbb{Z}^4.\\
&\text{2. Initialize }X^{(0)}\text{ from } \mathrm{SEED}.\\
&\text{3. For each construction round }k:\\
&\qquad
F_k
=
\{
c\in D:
\phi(c,k,\widetilde{X}^{(k)})=1
\}.\\
&\qquad
\text{Read all } \mathcal{N}_j(c;\widetilde{X}^{(k)})
\text{ from the old snapshot.}\\
&\qquad
\text{Update all } c\in F_k \text{ in parallel by } R.\\
&\qquad
\text{Copy all } c\notin F_k \text{ through unchanged.}
\end{aligned}
$$

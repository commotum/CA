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

At update time $t$, `FRONTIER` selects which current-state coordinates are active update sites. `NEIGHBORHOOD` reads around each selected current-state coordinate, `RULE` is applied in parallel, and the resulting values are written to the corresponding next-state coordinates at time $t+1$. Current-state sites not selected by the frontier are copied forward unchanged.

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

Each neighborhood is specified as a relative-offset read selector anchored at the current update site and built from the shared selector/mask utility:

```text
NEIGHBORHOOD[j]:
    SELECTOR[Q_N, C_N]
    Q_N = Z⁴
    C_N = (c, X̃⁽ᵗ⁾)
    VARIABLE = δ = [Δt, Δx, Δy, Δz]
    FRAME = RELATIVE_TO_SOURCE
    UNIVERSE = Ω_j : C_N → finite subsets of Z⁴
    PREDICATE = (η_j,1, ..., η_j,n)
    COMBINE = Ψ_j
    ORDER = ord_j
    READ_MODE ∈ {COMPACT_SELECTED, FIXED_SUPPORT_WITH_MASK}
```

Each frontier component is specified as an absolute-coordinate update-site selector built from the same selector/mask utility:

```text
FRONTIER[i]:
    SELECTOR[Q_F, C_F]
    Q_F = D
    C_F = (t, X̃⁽ᵗ⁾)
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

During generation, the partially written trajectory after completing updates through time $t$ is

$$
X^{(t)}:D\to A.
$$

All reads for the update from time $t$ to time $t+1$ are taken from a single boundary-extended snapshot

$$
\widetilde{X}^{(t)}:\mathbb{Z}^4\to A.
$$

The update time is the explicit time coordinate stored inside

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

Examples include binary states, $K$-color states, bounded integers, or symbolic states.

Formally,

$$
A
$$

is the cell-state alphabet, and every generated trajectory state is a map

$$
X^{(t)}:D\to A.
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

`BOUNDARY` defines how spatial reads behave outside `SHAPE` at the requested read time. The time coordinate is preserved; boundary policies act only on the active spatial axes.

Supported values:

```text
BOUNDARY ∈ {FIXED, PERIODIC, REFLECTIVE, CLAMP}
```

The boundary-extended field is

$$
\widetilde{X}^{(t)}:\mathbb{Z}^4\to A.
$$

Let

$$
c=[\tau,x,y,z]
$$

be a read coordinate whose time coordinate $\tau$ is available in the generated history, and let

$$
I_s=I_x\times I_y\times I_z.
$$

It is defined by

$$
\widetilde{X}^{(t)}(c)=
\begin{cases}
X^{(t)}(c),
& (x,y,z)\in I_s,\\
a_{\mathrm{bdry}},
& (x,y,z)\notin I_s
\ \land
\mathrm{BOUNDARY}=\mathrm{FIXED},\\
X^{(t)}\!\left(\operatorname{wrap}_s(c)\right),
& (x,y,z)\notin I_s
\ \land
\mathrm{BOUNDARY}=\mathrm{PERIODIC},\\
X^{(t)}\!\left(\operatorname{reflect}_s(c)\right),
& (x,y,z)\notin I_s
\ \land
\mathrm{BOUNDARY}=\mathrm{REFLECTIVE},\\
X^{(t)}\!\left(\operatorname{clamp}_s(c)\right),
& (x,y,z)\notin I_s
\ \land
\mathrm{BOUNDARY}=\mathrm{CLAMP}.
\end{cases}
$$

Here

$$
a_{\mathrm{bdry}}\in A
$$

is the fixed boundary value.

The helpers

$$
\operatorname{wrap}_s,\operatorname{reflect}_s,\operatorname{clamp}_s:\mathbb{Z}^4\to D
$$

preserve the time coordinate and act coordinatewise on the spatial intervals in `SHAPE`.

---

## NEIGHBORHOOD

`NEIGHBORHOOD` is an ordered collection of read stencils anchored at a current-state update site.

```text
NEIGHBORHOOD = (NEIGHBORHOOD[1], ..., NEIGHBORHOOD[m])
```

At update time $t$, a frontier-selected update site has coordinate

$$
c=[t,x,y,z].
$$

Each `NEIGHBORHOOD[j]` defines a finite, ordered relative-offset read interface around that current site. The offset coordinate is

$$
\delta=[\Delta t,\Delta x,\Delta y,\Delta z]\in\mathbb{Z}^4.
$$

The offset $\delta$ is interpreted relative to the current update site, not relative to the future write coordinate. Thus the queried coordinate is

$$
c+\delta=[t+\Delta t,\ x+\Delta x,\ y+\Delta y,\ z+\Delta z].
$$

For ordinary Wolfram-style cellular automata, spatial neighborhoods read the current state, so

```text
Δt = 0
```

for every spatial read. Temporal recurrences may additionally read past source times such as `Δt = -1`. Future reads with `Δt > 0` are non-causal for next-state generation.

`NEIGHBORHOOD` and `FRONTIER` use the same selector/mask utility. They remain semantically distinct: a neighborhood selects **relative offsets to read around a current update site**, while a frontier selects **absolute current-state sites allowed to update**.

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
- `FRAME` records whether the candidate is an absolute coordinate or a source-relative offset.
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

If `ORDER = NONE`, the selected value is semantically an unordered finite set. If an implementation needs deterministic enumeration for batching, logging, visualization, or reproducible stochastic sampling, it may still use an implementation-level canonical enumeration without changing the mathematical update semantics.

### Selector specialization for neighborhoods

For neighborhoods, the selector is specialized as follows:

```text
NEIGHBORHOOD[j]:
    SELECTOR[Q_N, C_N]
    Q_N = Z⁴
    C_N = (c, X̃⁽ᵗ⁾)
    VARIABLE = δ = [Δt, Δx, Δy, Δz]
    FRAME = RELATIVE_TO_SOURCE
    UNIVERSE = Ω_j : C_N → finite subsets of Z⁴
    PREDICATE = (η_j,1, ..., η_j,n)
    COMBINE = Ψ_j
    ORDER = ord_j
    READ_MODE ∈ {COMPACT_SELECTED, FIXED_SUPPORT_WITH_MASK}
```

The neighborhood context is

$$
C_N=(c,\widetilde{X}^{(t)}).
$$

Each predicate has type

$$
\eta_{j,\ell}:\mathbb{Z}^4\times C_N\to\{0,1\}.
$$

Equivalently,

$$
\eta_{j,\ell}(\delta,c,\widetilde{X}^{(t)})\in\{0,1\}.
$$

In the usual static-stencil case, predicates depend only on $\delta$:

$$
\eta_{j,\ell}(\delta)\in\{0,1\}.
$$

The selected offset sequence is

$$
N_j(c,\widetilde{X}^{(t)})
=
\operatorname{ord}_j\!\left(
\left\{
\delta\in\Omega_j(c,\widetilde{X}^{(t)}):
\Psi_j\!\left(
\eta_{j,1}(\delta,c,\widetilde{X}^{(t)}),
\dots,
\eta_{j,n_j}(\delta,c,\widetilde{X}^{(t)})
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
\Omega_j(c,\widetilde{X}^{(t)})\subset\mathbb{Z}^4.
$$

For static current-state neighborhoods, `UNIVERSE` is usually a fixed finite offset set $\Omega_j$. For example,

```text
UNIVERSE = {[0, Δx, Δy, 0] : Δx, Δy ∈ {-1,0,1}}
```

considers offsets on the current time slice, inside a $3\times3$ spatial window, with the $z$ axis inactive.

#### `PREDICATE`

`PREDICATE` decides whether a candidate offset is included. Predicates may be purely geometric, coordinate-dependent, time-dependent, or state-dependent:

```text
static stencil:                  η(δ)
coordinate-dependent stencil:    η(δ, c)
time-dependent stencil:          η(δ, c)
state-dependent adaptive stencil: η(δ, c, X̃⁽ᵗ⁾)
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
N_j(c,\widetilde{X}^{(t)})=(\delta_{j,1},\dots,\delta_{j,n}).
$$

The compact read vector is

$$
\mathcal{N}_j(c;\widetilde{X}^{(t)})
=
\left(
\widetilde{X}^{(t)}(c+\delta_{j,1}),
\dots,
\widetilde{X}^{(t)}(c+\delta_{j,n})
\right).
$$

If the selector is dynamic, the length $n$ may vary with $c$ or $\widetilde{X}^{(t)}$. Variable-length compact reads are most natural for `FORMULAIC`, `STOCHASTIC`, attention-like, or otherwise variable-arity rule implementations.

For lookup-based rule types such as `EXHAUSTIVE`, `ISOTROPIC`, fixed-arity `SEMI-TOTALISTIC`, and fixed-arity `TOTALISTIC` rules, `COMPACT_SELECTED` should use static or otherwise fixed-arity neighborhoods.

#### `READ_MODE = FIXED_SUPPORT_WITH_MASK`

This mode keeps a fixed read shape while allowing adaptive inclusion masks.

Let the neighborhood support be a fixed ordered sequence

$$
\Omega_j=(\omega_{j,1},\dots,\omega_{j,s})\subset\mathbb{Z}^4.
$$

The rule receives both the full support values

$$
V_j(c;\widetilde{X}^{(t)})
=
\left(
\widetilde{X}^{(t)}(c+\omega_{j,1}),
\dots,
\widetilde{X}^{(t)}(c+\omega_{j,s})
\right)
$$

and the inclusion mask

$$
M_j(c,\widetilde{X}^{(t)})
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
\eta_{j,1}(\omega_{j,a},c,\widetilde{X}^{(t)}),
\dots,
\eta_{j,n_j}(\omega_{j,a},c,\widetilde{X}^{(t)})
\right).
$$

The selected offsets are those support offsets whose mask entry equals 1. This mode is useful when the selector is adaptive but the rule still needs fixed-shape inputs.

In later `RULE` formulas, $\mathcal{N}_j$ denotes the neighborhood read object produced by the selected `READ_MODE`: either the compact value vector, or the fixed support values together with their mask.

### Boundary interaction

`NEIGHBORHOOD` chooses which offsets to read. `BOUNDARY` determines how reads behave when the queried coordinate lies outside $D$.

When $c+\delta\notin D$, the read is resolved by the boundary-extended field $\widetilde{X}^{(t)}$.

### Source-time causal convention

For Wolfram-style next-state generation, neighborhoods read from the current source state or from past source states.

If a current update site is

$$
c=[t,x,y,z],
$$

then a read offset

$$
\delta=[\Delta t,\Delta x,\Delta y,\Delta z]
$$

is source-time causal when

$$
\Delta t\le 0.
$$

The usual spatial cellular-automaton case uses $\Delta t=0$: the current state $s_t$ determines the next state $s_{t+1}$. Temporal-memory systems such as a second-order recurrence may use offsets like $\Delta t=0$ and $\Delta t=-1$ when computing the next value.

### Predicate macros

The macro layer includes `RADIUS`, `METRIC`, `REGION`, `FOV`, and axis-scoped `CHANGE_COUNT`. These are reusable predicate macros rather than primitive neighborhood fields.

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

Because the axes are explicit, temporal offsets such as $\Delta t=-1$ do not affect spatial change-count predicates unless `t` is explicitly included in the axis set.

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
TIME_OFFSET(h):          Δt = h
ZERO_AXES(B):            Δa = 0 for every a ∈ B
NONZERO(axes=B):         exists a ∈ B such that Δa ≠ 0
CURRENT_SPATIAL_CENTER:  Δt = 0 and Δx = Δy = Δz = 0 on active spatial axes
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

The examples assume Wolfram-style next-state generation, so spatial neighborhoods read from the current source state:

```text
Δt = 0
```

### Example: Moore neighborhood in 2D

The proper 2D Moore neighborhood is the eight surrounding cells on the current time slice.

```text
NEIGHBORHOOD Moore2D:
    SELECTOR[Q_N, C_N]
    Q_N = Z⁴
    C_N = (c, X̃⁽ᵗ⁾)
    VARIABLE = δ
    FRAME = RELATIVE_TO_SOURCE

    UNIVERSE =
        {[0, Δx, Δy, 0] :
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
[0,-1,-1,0]   SW
[0,-1, 0,0]   W
[0,-1, 1,0]   NW
[0, 0,-1,0]   S
[0, 0, 1,0]   N
[0, 1,-1,0]   SE
[0, 1, 0,0]   E
[0, 1, 1,0]   NE
```

For the nine-cell current-state spatial stencil, including the current spatial center `[0,0,0,0]`, remove `PREDICATE[2]`.

### Example: Von Neumann neighborhood in 2D

The proper 2D Von Neumann neighborhood is the four cardinal cells on the current time slice.

```text
NEIGHBORHOOD VonNeumann2D:
    SELECTOR[Q_N, C_N]
    Q_N = Z⁴
    C_N = (c, X̃⁽ᵗ⁾)
    VARIABLE = δ
    FRAME = RELATIVE_TO_SOURCE

    UNIVERSE =
        {[0, Δx, Δy, 0] :
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
[0,-1, 0,0]   W
[0, 0,-1,0]   S
[0, 0, 1,0]   N
[0, 1, 0,0]   E
```

### Example: current self only

Useful when the source cell's current state should be separated from its surrounding neighbors.

```text
NEIGHBORHOOD CurrentSelf:
    SELECTOR[Q_N, C_N]
    Q_N = Z⁴
    C_N = (c, X̃⁽ᵗ⁾)
    VARIABLE = δ
    FRAME = RELATIVE_TO_SOURCE

    UNIVERSE = {[0,0,0,0]}

    PREDICATE[1](δ) = true

    COMBINE = IDENTITY
    ORDER = LEX(Δt, Δx, Δy, Δz)
    READ_MODE = COMPACT_SELECTED
```

A Life-like or semi-totalistic rule can then use:

```text
NEIGHBORHOOD[1] = CurrentSelf
NEIGHBORHOOD[2] = Moore2D
```

instead of using a single current-state spatial stencil that includes the current spatial center.

### Example: Dyadaxes neighborhoods

The V1.1 Dyadaxes family uses three current-state neighborhood components.

In `t+1D`:

```text
CurrentSelf = {[0,  0,0,0]}
Primary     = {[0, -1,0,0], [0, +1,0,0]}
Secondary   = {[0, -2,0,0], [0, +2,0,0]}
```

In `t+2D`:

```text
CurrentSelf = {[0,  0,  0,0]}
Primary     = RADIUS(axes={x,y}, METRIC=L1,   REGION=SHELL,  r=1)
Secondary   = CHANGE_COUNT(axes={x,y}, K={2}) inside the 3x3 current-state window
```

In `t+3D`:

```text
CurrentSelf = {[0, 0, 0, 0]}
Primary     = RADIUS(axes={x,y,z}, METRIC=L1,   REGION=SHELL,  r=1)
Secondary   = CHANGE_COUNT(axes={x,y,z}, K={2,3}) inside the 3x3x3 current-state window
```

A second-order scalar recurrence can use source-time memory by reading the current scalar and the previous scalar:

```text
Current = {[0, 0,0,0]}
Prev    = {[-1,0,0,0]}
```

---

## FRONTIER

`FRONTIER` is an ordered collection of absolute-coordinate update-site selectors.

```text
FRONTIER = (FRONTIER[1], ..., FRONTIER[q])
```

Each `FRONTIER[i]` selects current-state update sites

$$
c=[t,x,y,z]\in D
$$

from the persistent trajectory domain. Unlike neighborhoods, frontiers select absolute current coordinates, not relative offsets. The write coordinate associated with an update site is

$$
c^+=[t+1,x,y,z].
$$

### Selector specialization for frontiers

For frontiers, the shared selector is specialized as follows:

```text
FRONTIER[i]:
    SELECTOR[Q_F, C_F]
    Q_F = D
    C_F = (t, X̃⁽ᵗ⁾)
    VARIABLE = c = [t, x, y, z]
    FRAME = ABSOLUTE
    UNIVERSE = U_i : C_F → finite subsets of D
    PREDICATE = (φ_i,1, ..., φ_i,n)
    COMBINE = Φ_i
    ORDER = ord_i
```

Each predicate has type

$$
\phi_{i,\ell}:D\times C_F\to\{0,1\}.
$$

Equivalently,

$$
\phi_{i,\ell}(c,t,\widetilde{X}^{(t)})\in\{0,1\}.
$$

If a frontier predicate is purely geometric or time-scheduled, it may ignore $\widetilde{X}^{(t)}$.

The component update-site set is

$$
F_{i,t}
=
\left\{
c\in U_i(t,\widetilde{X}^{(t)}):
\Phi_i\!\left(
\phi_{i,1}(c,t,\widetilde{X}^{(t)}),
\dots,
\phi_{i,n_i}(c,t,\widetilde{X}^{(t)})
\right)=1
\right\}.
$$

A top-level Boolean combiner

$$
\Phi_{\mathrm{frontier}}:\{0,1\}^q\to\{0,1\}
$$

combines the component frontiers into the active frontier predicate:

$$
\phi(c,t,\widetilde{X}^{(t)})
=
\Phi_{\mathrm{frontier}}\!\left(
\mathbf{1}[c\in F_{1,t}],
\dots,
\mathbf{1}[c\in F_{q,t}]
\right).
$$

The active update-site set at time $t$ is

$$
S_t=\{[t,x,y,z]\in D\}.
$$

$$
F_t
=
\{c\in S_t:\phi(c,t,\widetilde{X}^{(t)})=1\}.
$$

All coordinates in $F_t$ are updated in parallel from the same current snapshot $\widetilde{X}^{(t)}$ and written to their corresponding next-time coordinates $c^+$.

### Defaults

```text
UNIVERSE = current time slice { [t,x,y,z] }
COMBINE = IDENTITY        if there is one predicate
COMBINE = AND             if multiple predicates are listed without another combiner
ORDER = NONE
FRONTIER_COMBINE = OR
```

Inside one frontier selector, `COMBINE` combines that selector's predicates. Across multiple frontier components, `FRONTIER_COMBINE` combines the component update-site sets.

`ORDER = NONE` means frontier order has no mathematical effect because writes are parallel. An implementation may still use a deterministic enumeration such as lexicographic order for batching, logging, visualization, or reproducible stochastic sampling.

### Example: Full current-state update slice

This is the standard cellular-automaton update schedule.

```text
FRONTIER FullCurrentSlice:
    SELECTOR[Q_F, C_F]
    Q_F = D
    C_F = (t, X̃⁽ᵗ⁾)
    VARIABLE = c
    FRAME = ABSOLUTE

    UNIVERSE = {[t,x,y,z] : (x,y,z) in active spatial domain}

    PREDICATE[1](c,t,X̃) = true

    COMBINE = IDENTITY
    ORDER = NONE
```

At time $t$, this selects

$$
F_t=\{[t,x,y,z]\in D\}.
$$

The rule writes the selected sites to

$$
F_t^+=\{[t+1,x,y,z]:[t,x,y,z]\in F_t\}.
$$

### Example: Single row in a 2D current slice

This updates only row $y=y_0$ of the current slice and writes the result to the same row in the next slice.

```text
FRONTIER SingleRow2D:
    SELECTOR[Q_F, C_F]
    Q_F = D
    C_F = (t, X̃⁽ᵗ⁾)
    VARIABLE = c
    FRAME = ABSOLUTE

    UNIVERSE = {[t,x,y,0] : x ∈ I_x, y ∈ I_y}

    PREDICATE[1](c,t,X̃) =
        y = y₀

    COMBINE = IDENTITY
    ORDER = NONE
```

The update-site set is

$$
F_t=\{[t,x,y_0,0]\in D\}.
$$

### Example: Checkerboard sublattice in the current slice

This updates alternating spatial cells and writes them to the next slice.

```text
FRONTIER Checkerboard2D:
    SELECTOR[Q_F, C_F]
    Q_F = D
    C_F = (t, X̃⁽ᵗ⁾)
    VARIABLE = c
    FRAME = ABSOLUTE

    UNIVERSE = {[t,x,y,0] : x ∈ I_x, y ∈ I_y}

    PREDICATE[1](c,t,X̃) =
        (x + y) mod 2 = 0

    COMBINE = IDENTITY
    ORDER = NONE
```

Alternating checkerboards by current time can be written as:

```text
(x + y) mod 2 = t mod 2
```

### Example: State-dependent active wavefront

This updates current-slice coordinates adjacent to active cells in the current state.

```text
FRONTIER ActiveWavefront2D:
    SELECTOR[Q_F, C_F]
    Q_F = D
    C_F = (t, X̃⁽ᵗ⁾)
    VARIABLE = c
    FRAME = ABSOLUTE

    UNIVERSE = {[t,x,y,0] : x ∈ I_x, y ∈ I_y}

    PREDICATE[1](c,t,X̃) =
        exists δ ∈ AdjacentCurrent2D :
            X̃(c + δ) = a_active

    COMBINE = IDENTITY
    ORDER = NONE
```

where

```text
AdjacentCurrent2D =
    { [0,-1,0,0],
      [0, 1,0,0],
      [0,0,-1,0],
      [0,0, 1,0] }
```

This is a wavefront frontier: the update-site region depends on the already generated current slice.

---

## RULE

`RULE` maps neighborhood reads at a current update site to the value written at the corresponding next-state site.

All rule types are filtered by `NEIGHBORHOOD`. They differ only in how the local input is represented before the output is selected.

For a current-state coordinate in the current slice

$$
c=[t,x,y,z],
$$

let the corresponding next-state coordinate be

$$
c^+=[t+1,x,y,z].
$$

The generator update is

$$
X^{(t+1)}(c^+)=
\begin{cases}
R\!\left(
c,
\widetilde{X}^{(t)},
\mathcal{N}_1(c;\widetilde{X}^{(t)}),
\dots,
\mathcal{N}_m(c;\widetilde{X}^{(t)})
\right),
& c\in F_t,\\
X^{(t)}(c),
& c\in S_t\setminus F_t.
\end{cases}
$$

All coordinates in $F_t$ are updated in parallel from the same current snapshot $\widetilde{X}^{(t)}$.

---

## RULETYPE = EXHAUSTIVE

`EXHAUSTIVE` is a lookup table over the full ordered local pattern.

Let

$$
\mathcal{N}(c;\widetilde{X}^{(t)})
=
\left(
\mathcal{N}_1(c;\widetilde{X}^{(t)}),
\dots,
\mathcal{N}_m(c;\widetilde{X}^{(t)})
\right).
$$

An exhaustive rule is

$$
R(c,\widetilde{X}^{(t)},\mathcal{N})
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
R(c,\widetilde{X}^{(t)},\mathcal{N})
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
R(c,\widetilde{X}^{(t)},\mathcal{N})
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

A common binary case keeps the center state explicit and aggregates the surrounding cells by active count. For a single neighborhood $N$, let $S=\{s\}$ be a singleton designated subset corresponding to the current self entry, and let $B=N\setminus S$. Then

$$
R(c,\widetilde{X}^{(t)},\mathcal{N})
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

If $s$ is the current self entry, then $\mathcal{N}_{s}=\widetilde{X}^{(t)}(c)$. This is the usual outer-totalistic form: the rule depends on the center state and on a totalistic summary of the outer neighborhood.

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
R(c,\widetilde{X}^{(t)},\mathcal{N})
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
R(c,\widetilde{X}^{(t)},\mathcal{N})
=
f\!\left(
c,
\widetilde{X}^{(t)},
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
R(c,\widetilde{X}^{(t)},\mathcal{N})
\sim
P\!\left(
\cdot
\mid
c,
\widetilde{X}^{(t)},
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

## Wolfram / Transformer Next-State Convention

The default trajectory-generation setting stores the full state at every causal coordinate $t$.

The state at time $t$ determines the state at time $t+1$:

$$
X_{t+1}=\mathcal{R}(X_{\le t}).
$$

For ordinary cellular automata, the rule reads the current source state:

$$
\Delta t=0.
$$

For temporal recurrences, the rule may additionally read past source states:

$$
\Delta t\le 0.
$$

For Wolfram elementary cellular automata, this is the usual form

$$
a_i(t+1)
=
F\!\left(
a_{i-1}(t),
a_i(t),
a_{i+1}(t)
\right).
$$

In transformer training terms, the model consumes state-token coordinates at time $t$ and predicts the corresponding state-token coordinates at time $t+1$. The generator uses explicit state coordinates rather than relying on a flat token order to express this causality.

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

Its generation semantics are:

$$
\begin{aligned}
&\text{1. Allocate }D\subseteq\mathbb{Z}^4.\\
&\text{2. Initialize }X^{(0)}\text{ from } \mathrm{SEED}.\\
&\text{3. For each update time }t=0,\dots,T-2:\\
&\qquad
S_t
=
\{
c\in D:
\mathrm{time}(c)=t
\}.\\
&\qquad
F_t
=
\{
c\in S_t:
\phi(c,t,\widetilde{X}^{(t)})=1
\}.\\
&\qquad
\text{Read all } \mathcal{N}_j(c;\widetilde{X}^{(t)})
\text{ from the current snapshot.}\\
&\qquad
\text{Write all } c^+=[t+1,x,y,z] \text{ for } c\in F_t \text{ in parallel by } R.\\
&\qquad
\text{Copy all } c^+=[t+1,x,y,z] \text{ for } c\in S_t\setminus F_t \text{ forward unchanged.}
\end{aligned}
$$

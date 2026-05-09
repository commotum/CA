• Based on CA-Types.md:18 and NKS, I’d standardize the
  alphabet/value-space types like this:

  | Type | Meaning | Examples |
  | --- | --- | --- |
  | binary | Two states, usually 0/1 or white/black |
  elementary CA, many 2D CAs |
  | k_color | Finite color/state set {0, ..., k-1} | 3-
  color, 4-color, 5-color CAs |
  | ordered_k_color | k_color where numeric order matters |
  totalistic rules using sums/averages |
  | symbolic | Finite labels with no numeric meaning | A/B,
  substitution systems, tag systems, multiway strings |
  | digit_base | Positional digits {0, ..., b-1} with base
  semantics | binary/decimal digit systems, digit-reversal
  systems |
  | tape_symbol | Symbol alphabet plus a blank symbol |
  Turing machine tapes |
  | head_state | Finite machine-control states | Turing
  machine heads, active automata state |
  | integer | Unbounded integer value space | registers,
  integer maps, number filters |
  | real_interval | Continuous scalar range, usually [0, 1]
  | continuous cellular automata, iterated maps |
  | expression_atom | Atoms/operators in expression trees |
  symbolic systems |
  | graph_label | Node or edge labels | network systems |
  | continuous_field | Field/function values over continuous
  space/time | PDE systems |

  For a CA-focused API, the practical core is probably:

  binary
  k_color
  ordered_k_color
  symbolic
  digit_base
  integer
  real_interval

  Then model tape_symbol, head_state, expression_atom,
  graph_label, and continuous_field as engine-specific
  extensions.

  Important distinction: totalistic is not an alphabet type.
  It is a rule form over an ordered numeric alphabet.
  Likewise, quiescent or blank is not an alphabet type; it
  is a distinguished state inside an alphabet. CA-Types
  makes that separation explicit around alphabet/value
  space, rule form, and background state in CA-Types.md:18.

  ---

  › couldn't tape symbol or head state, aren't those just
  multi-value cells?

  ---

• Yes. At the value level, tape_symbol and head_state are
  just finite multi-value states.

  The distinction I was making is semantic/API-level, not
  mathematical necessity:

  - A tape symbol is a finite cell value: {0, 1}, {blank,
    mark}, {A, B, C}, etc.
  - A head state is also finite: {q0, q1, q2, ...}.
  - But in a Turing machine, the head state is not normally
    a value stored in every tape cell. It is control state
    attached to one active position.

  You can absolutely encode a Turing machine as a cellular
  automaton by making each cell’s alphabet composite, for
  example:

  CellAlphabet =
    TapeSymbol
    union
    (TapeSymbol x HeadState)

  So most cells contain only a tape symbol, and exactly one
  cell contains both a tape symbol and a head state.

  A cleaner standard taxonomy would be:

  | Alphabet Type | Meaning |
  | --- | --- |
  | binary | finite alphabet of size 2 |
  | finite_categorical | finite unordered symbols/colors |
  | finite_ordered | finite numeric states {0,...,k-1} where
  order/sum matters |
  | digit_base | finite ordered alphabet with positional
  base semantics |
  | finite_composite | product/sum of finite layers, e.g.
  tape symbol + optional head state |
  | integer | unbounded discrete numeric value |
  | real_interval | continuous scalar value, usually [0,1] |
  | structured | expression/tree/graph values built from
  finite atoms |

  So yes: tape_symbol and head_state should not be top-level
  alphabet types. They are better modeled as roles inside a
  finite or composite alphabet.
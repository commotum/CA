# Cellular Automata and Adjacent Simple Program Construction Types

Source scope:

- `A New Kind of Science/CHAPTERS/The-World-of-Simple-Programs/The-World-of-Simple-Programs.md`
- `A New Kind of Science/CHAPTERS/Systems-Based-on-Numbers/Systems-Based-on-Numbers.md`
- `A New Kind of Science/CHAPTERS/Two-Dimensions-and-Beyond/Two-Dimensions-and-Beyond.md`

This index classifies cellular automata, adjacent simple-program systems, number-based systems, and continuous systems by how they are built: data structure, states or value space, neighborhood or access pattern, rule form, update schedule, coding scheme, and initial-condition convention. It deliberately avoids behavior-based classes such as repetitive, nested, random, or localized-structure behavior.

## Core Construction Axes

| Axis | Construction Question |
| --- | --- |
| Dimension | Is the system one-dimensional, two-dimensional, three-dimensional, higher-dimensional, or dimensionless? |
| Geometry | Are components arranged on a line, square grid, triangular grid, hexagonal grid, cubic lattice, arbitrary lattice, network, sequence, or continuous field? |
| Lattice | Are components arranged on a fixed lattice, or can the number/organization of elements change? |
| Alphabet or value space | How many possible states, colors, symbols, or values can each component have? |
| Neighborhood | Which previous cells can affect the next state of a cell? |
| Rule form | Does the rule distinguish ordered neighborhoods, or only totals/averages? |
| Update schedule | Are all cells updated in parallel, only selected active cells, one sequence term, one number, or a continuous field? |
| Background | Is there a designated blank state that remains blank in a blank neighborhood? |
| Initial condition | Is the run started from a single nonblank cell, a random configuration, or another seed? |

## 1. Elementary Cellular Automata

Construction:

- One-dimensional fixed line of cells.
- Two possible cell states, usually represented as white/black or 0/1.
- Nearest-neighbor local rule: the next state of a cell depends on the previous state of its left neighbor, itself, and its right neighbor.
- All cells update in parallel at every step.
- The rule is an arbitrary map from the 8 ordered three-cell neighborhoods to one of the 2 states.

Rule count:

- `2^(2^3) = 256` possible rules.
- Wolfram numbers them `0` through `255` by reading the 8 output choices as binary digits.
- Under left-right reflection and black-white interchange, the 256 rules reduce to 88 fundamentally inequivalent rules.

Chapter 3 run convention:

- Usually started from a single black cell on a white background.

## 2. Multi-Color Nearest-Neighbor Cellular Automata

Construction:

- Same one-dimensional fixed lattice as elementary cellular automata.
- Same parallel update schedule.
- Same radius-1 neighborhood: left cell, center cell, right cell.
- More than two possible cell states.
- The rule is an arbitrary map from each ordered three-cell neighborhood to one output state.

Rule count:

- For `k` colors, there are `k^3` possible ordered neighborhoods.
- Each neighborhood can map to any of `k` output colors.
- Total rule count: `k^(k^3)`.
- For `k = 3`, this gives `3^27 = 7,625,597,484,987` possible rules.

What makes this construction different:

- It increases the cell alphabet.
- It keeps ordered neighborhood dependence, so `012`, `021`, and `102` can all be assigned different outputs.
- It keeps the rigid lattice and parallel update structure of elementary cellular automata.

## 3. Totalistic Cellular Automata

Construction:

- One-dimensional fixed line of cells.
- `k` possible cell states, encoded numerically as `0` through `k - 1`.
- Nearest-neighbor radius-1 update using the left cell, center cell, and right cell.
- All cells update in parallel.
- The rule depends only on the sum or average of the three neighborhood values, not on their ordered arrangement.

Rule count:

- Possible sums range from `0` to `3(k - 1)`.
- Number of sum cases: `3k - 2`.
- Each sum case can map to any of `k` states.
- Total rule count: `k^(3k - 2)`.

Examples from the chapter:

- `k = 2`: `2^4 = 16` totalistic rules.
- `k = 3`: `3^7 = 2187` totalistic rules.
- `k = 5`: `5^13 = 1,220,703,125` totalistic rules.

Coding convention:

- The rule can be encoded as a base-`k` digit sequence.
- For three-color totalistic rules, the rightmost digit gives the output for average color `0`; digits to the left give outputs for increasing average values.

What makes this construction different:

- It collapses ordered neighborhoods that have the same sum or average.
- It is left-right symmetric by construction, because reversing the neighborhood does not change the sum.
- It gives a much smaller rule space than full ordered-neighborhood multi-color cellular automata.

## 4. Three-Color Totalistic Cellular Automata

Construction:

- A concrete totalistic case emphasized in Chapter 3.
- One-dimensional fixed line.
- Three states, usually shown as white, gray, and black, or encoded as `0`, `1`, and `2`.
- Parallel nearest-neighbor update.
- The output depends only on the average or sum of the three neighboring values.

Rule count:

- Seven possible neighborhood sums: `0` through `6`.
- `3^7 = 2187` possible rules.

Chapter 3 run convention:

- Usually started from a single gray cell on a white background.
- Some displayed scans exclude rules that change the all-white background.

What makes this construction different:

- It is the smallest totalistic alphabet size in the chapter where Wolfram emphasizes a much larger rule space than the elementary rules while still keeping the rule compact enough to survey.

## 5. Higher-Color Totalistic Cellular Automata

Construction:

- Same as totalistic cellular automata, but with four, five, or more states.
- Still a one-dimensional fixed lattice.
- Still parallel nearest-neighbor update.
- Still sum/average-based rather than ordered-neighborhood-based.

Rule count:

- General count: `k^(3k - 2)`.
- The chapter explicitly notes the five-color case: `5^13 = 1,220,703,125` possible rules.

What makes this construction different:

- It increases the number of possible states and the number of sum cases.
- It does not change the lattice, neighborhood radius, totalistic restriction, or parallel update scheme.

## 6. Quiescent-Background-Preserving Cellular Automata

This is a construction filter, not a separate architecture.

Construction criterion:

- A designated blank state remains blank when all cells in the neighborhood are blank.
- For two-color elementary rules, this means the `000` neighborhood maps to `0`.
- For totalistic rules, this means sum `0` maps to state `0`.

Why it matters structurally:

- It allows finite nonblank seeds to be studied against a stable blank background.
- Without this filter, the blank background itself changes immediately, so the experiment is no longer a localized seed evolving into a blank environment.

## 7. Left-Right Symmetric Cellular Automata

This is also a construction filter, not a separate architecture.

Construction criterion:

- Reversing the left and right neighbors does not change the rule output.
- In elementary rules, the output for each neighborhood `abc` must match the output for `cba`.
- Totalistic nearest-neighbor rules automatically satisfy this criterion because they depend only on sums or averages.

What makes this construction different:

- The local rule cannot distinguish left from right.
- Wolfram notes that early searches focused on rules with left-right symmetry and stable blank backgrounds, a much smaller subset than all 256 elementary rules.

## 8. Initial-Condition Classes

Initial conditions are not cellular automaton types, but they are part of the construction of an experiment.

Common Chapter 3 conventions:

- Single black cell in a white background for elementary cellular automata.
- Single gray cell in a white background for three-color totalistic cellular automata.
- Random initial conditions are mentioned as a separate experimental setup.

Why they matter structurally:

- The same rule can be run from different initial configurations.
- A taxonomy of automata should keep the rule construction separate from the initial condition used to probe it.

## Adjacent Simple-Program Systems In Chapter 3

Chapter 3 uses the following systems to remove or alter specific construction assumptions from cellular automata. They are adjacent to cellular automata because they still use precise local or rule-based evolution, but most are not cellular automata in the strict fixed-lattice, parallel-update sense.

| System | Core Data Structure | Main Construction Difference From Cellular Automata |
| --- | --- | --- |
| Mobile automata | Fixed one-dimensional cell line plus one active cell | Only the active cell is updated; the rule also moves the active cell. |
| Extended mobile automata | Fixed one-dimensional cell line plus one active cell | The active cell and nearby cells can be updated together. |
| Generalized mobile automata | Fixed one-dimensional cell line plus many possible active cells | Active cells can proliferate, move, split, or disappear. |
| Turing machines | Fixed tape plus stateful head | Rule sees head state and current tape cell, not a whole neighborhood. |
| Substitution systems | Variable-length sequence | Elements are replaced by blocks, so the number of elements changes. |
| Sequential substitution systems | Variable-length string | One matching substring is replaced per step, in scan order. |
| Tag systems | Queue-like sequence | Elements are removed from the front and appended to the end. |
| Cyclic tag systems | Queue-like sequence plus cyclic program counter | The append rule is chosen cyclically rather than by a full local neighborhood. |
| Register machines | Finite list of unbounded integer registers | Evolution follows an instruction pointer and numeric register operations. |
| Symbolic systems | Tree-like symbolic expressions | Rewrite rules act on expression patterns, often non-locally. |

## 9. Mobile Automata

Construction:

- One-dimensional fixed line of cells.
- In the chapter's basic setup, each cell has two possible colors.
- At any step, exactly one cell is marked as active.
- The rule is applied only at the active cell.
- The rule input is the color of the active cell and its immediate left and right neighbors.
- The rule output specifies two things:
  - the new color of the active cell;
  - whether the active cell moves left or right for the next step.

Rule count:

- Chapter 3 gives `65,536` rules for the basic two-color, nearest-neighbor, single-active-cell construction.

What makes this construction different:

- Cellular automata update all cells in parallel; mobile automata update one active position at a time.
- The active position is part of the system state.
- Motion is built into the rule, so rule outputs include both cell-writing and head-movement information.

API shape:

- `states`: cell colors.
- `active_position`: integer position of the active cell.
- `read_window`: usually radius-1 around the active cell.
- `write_scope`: active cell only.
- `move_set`: usually `{left, right}`.
- `rule`: map from read-window configuration to `{new_color, move}`.

## 10. Extended Mobile Automata

Construction:

- Same fixed one-dimensional cell line as mobile automata.
- Same single active cell.
- The rule can update more than just the active cell.
- In Chapter 3's extension, the rule may update the active cell and its immediate neighbors.
- The rule still controls active-cell movement.

Rule count:

- Chapter 3 gives `4,294,967,296` rules for the extension that allows the active cell and its immediate neighbors to be updated.

What makes this construction different:

- It widens the write scope while keeping a single active position.
- A basic mobile automaton reads a local neighborhood but writes only one cell.
- An extended mobile automaton reads and writes a local block around the active cell.

API shape:

- `read_window`: local block around the active cell.
- `write_window`: local block, such as left/center/right.
- `move_set`: active-cell movement choices.
- `rule`: map from local configuration to `{replacement_block, move}`.

## 11. Generalized Mobile Automata

Construction:

- Fixed one-dimensional line of colored cells.
- Any number of cells can be active at the same time.
- The rule is applied to active cells.
- The rule can cause active cells to move, split into multiple active cells, or disappear.
- Activity is therefore a second layer of state over the cell colors.

What makes this construction different:

- Ordinary mobile automata have exactly one active cell.
- Generalized mobile automata allow an active set.
- Cellular automata can be seen as a limiting case where many or all cells are active at each step.

API shape:

- `states`: cell colors.
- `active_set`: set of active positions.
- `read_window`: local neighborhood around each active position.
- `write_policy`: how simultaneous writes are resolved if active neighborhoods overlap.
- `activity_rule`: movement, splitting, survival, or deletion of active markers.

Implementation note:

- A generalized mobile automaton needs an explicit conflict policy if two active cells attempt to write the same site in the same step. Chapter 3's conceptual setup focuses on examples where the visual rule resolves this, but an API should make it explicit.

## 12. Turing Machines

Construction:

- One-dimensional tape of cells.
- Each tape cell has a color or symbol.
- A single active head sits at one tape position.
- The head has an internal state.
- The rule input is only:
  - current head state;
  - current tape-cell symbol.
- The rule output specifies:
  - symbol to write at the current tape cell;
  - direction for the head to move;
  - new head state.

Rule counts and thresholds mentioned:

- With two head states and two tape colors, Chapter 3 notes `4096` possible machines.
- With three head states, there are about three million possible machines.
- Four head states produce a much larger rule space and are the first head-state count in the chapter where Wolfram reports finding more complex examples from a blank tape.

What makes this construction different:

- A mobile automaton's rule can look at neighboring cell colors; a Turing machine's rule normally cannot.
- A Turing machine compensates by giving the head internal state.
- The local tape structure remains fixed, but the active head carries memory.

API shape:

- `symbols`: tape alphabet.
- `head_states`: finite state set.
- `blank_symbol`: default tape value.
- `head_position`: integer.
- `initial_head_state`: starting state.
- `rule`: map from `{head_state, current_symbol}` to `{write_symbol, move, next_head_state}`.

## 13. Neighbor-Independent Substitution Systems

Construction:

- Variable-length sequence of elements.
- Each element has a color or symbol.
- At each step, every element is replaced in parallel by a block of elements.
- The replacement for an element depends only on that element's own symbol.
- Neighboring elements do not affect the replacement.

Examples of rule form:

- `A -> AB`
- `B -> A`
- Or, in color language, each color maps to a fixed block of colors.

What makes this construction different:

- Cellular automata preserve the number and positions of cells; substitution systems can change sequence length.
- The update is still parallel, but it is a replacement of elements by blocks rather than a state update on fixed sites.
- Because replacements are independent of neighbors, the construction is especially close to formal grammars and morphisms.

API shape:

- `symbols`: element alphabet.
- `rule`: map from each symbol to an output word.
- `initial_word`: starting sequence.
- `update`: parallel replacement of all symbols.

Rendering note:

- Chapter 3 shows two useful renderings:
  - fixed-size symbols, where the row grows wider;
  - rescaled subdivision, where the whole row keeps constant width.

## 14. Neighbor-Dependent Substitution Systems

Construction:

- Variable-length sequence of symbols.
- Elements are replaced by blocks in parallel.
- The replacement can depend on neighboring symbols.
- Chapter 3 gives examples where replacing an element depends on the element itself and the symbol immediately to its right.
- Boundary handling is part of the construction; in the displayed examples, the rightmost element is dropped when no right neighbor exists.

What makes this construction different:

- It removes the fixed lattice assumption of cellular automata, but keeps local neighbor dependence.
- Unlike neighbor-independent substitution, an element's replacement is contextual.
- Unlike cellular automata, each replacement can change the number of elements.

API shape:

- `symbols`: element alphabet.
- `context`: for example `(current, right_neighbor)`.
- `boundary_policy`: drop, pad with blank, wrap, or use a special boundary symbol.
- `rule`: map from context to replacement word.
- `update`: parallel replacement of all eligible contexts.

## 15. Creation-Destruction Substitution Systems

Construction:

- Variable-length symbol sequence.
- Replacement blocks may be empty.
- Empty replacement means the original element disappears.
- Non-empty replacement can create one or more elements.
- Rules can therefore balance growth and shrinkage.

What makes this construction different:

- Standard cellular automata conserve the number of cells.
- Ordinary substitution systems usually grow or maintain length if every replacement has length at least one.
- Creation-destruction substitution systems allow local deletion, making total length a dynamic quantity.

API shape:

- `symbols`: alphabet.
- `rule`: map from symbol or context to replacement word, where `""` is allowed.
- `growth_policy`: no separate policy is needed mathematically, but experiments may filter for bounded, slow-growth, or non-extinct runs.
- `rendering`: fixed-width rows, rescaled rows, or event/compressed views.

## 16. Sequential Substitution Systems

Construction:

- Variable-length string over a finite alphabet.
- A rule consists of one or more ordered replacements.
- At each step, the system scans the string from left to right.
- It applies the first replacement that can be used, at the first matching position according to the scan convention.
- Only one replacement event occurs per step.

Example from Chapter 3:

- Replace the first occurrence of `BA` with `ABA`.

What makes this construction different:

- Ordinary substitution systems apply replacements everywhere in parallel.
- Sequential substitution systems apply one local text-edit operation at a time.
- The order of replacement rules and the scan direction are part of the construction.

API shape:

- `symbols`: alphabet.
- `replacements`: ordered list such as `[("ABA", "AAB"), ("A", "ABA")]`.
- `scan_direction`: usually left-to-right.
- `match_policy`: first matching rule, first matching position.
- `initial_word`: starting string.

## 17. Tag Systems

Construction:

- Variable-length sequence of symbols.
- At each step, remove a fixed number of symbols from the beginning of the sequence.
- The removed symbols determine which block is appended to the end.
- The system halts or becomes extinct if too few symbols remain to remove.

Chapter 3 variants:

- One-symbol deletion tag systems.
- Two-symbol deletion tag systems.

What makes this construction different:

- A tag system is queue-like: consume from the front, append at the back.
- There is no spatially fixed neighborhood.
- The rule input is the deleted prefix, not a local neighborhood centered at each site.
- The rule output is an appended block, not a replacement in place.

API shape:

- `symbols`: alphabet.
- `deletion_number`: number of symbols removed each step.
- `append_rule`: map from removed prefix to appended word.
- `initial_word`: starting sequence.
- `halt_policy`: stop if length is less than `deletion_number`.

## 18. Cyclic Tag Systems

Construction:

- Variable-length sequence of symbols.
- A cyclic list of append blocks acts like a program counter.
- At each step:
  - remove one symbol from the beginning;
  - advance to the next append block in the cycle;
  - append the current block only if the removed symbol satisfies the trigger condition, such as being black.

What makes this construction different:

- Ordinary tag systems choose the appended block from the deleted symbols.
- Cyclic tag systems choose the possible appended block from a cyclic schedule.
- The deleted symbol controls whether the scheduled block is appended, not which block is scheduled.

API shape:

- `symbols`: usually includes a blank/white and active/black symbol.
- `program`: cyclic list of append words.
- `trigger_symbol`: symbol that causes append.
- `deletion_number`: typically 1 in the Chapter 3 setup.
- `program_counter`: current position in the cyclic list.

## 19. Register Machines

Construction:

- A finite set of registers.
- Each register stores a non-negative integer of unbounded size.
- A program is a finite sequence of instructions.
- An instruction pointer chooses the next instruction.
- Chapter 3 focuses on two registers and two instruction types:
  - increment a specified register;
  - decrement a specified register and jump to a specified instruction if the decrement succeeds.
- If a decrement is attempted on a zero register, the register remains zero and execution continues without the jump.

What makes this construction different:

- There is no spatial cell lattice.
- State is numeric rather than a sequence of colored cells.
- Conditional control flow comes from whether a register is zero.
- The program text is fixed; the evolving state is the register values plus the instruction pointer.

API shape:

- `registers`: number of registers.
- `initial_values`: starting non-negative integers.
- `instructions`: ordered instruction list.
- `instruction_pointer`: current instruction.
- `instruction_set`: operations such as increment and decrement-jump.
- `zero_policy`: decrement on zero falls through without changing the register.

## 20. Symbolic Systems

Construction:

- State is a symbolic expression rather than a cell array or string alone.
- Expressions may be represented as nested trees, such as combinator-like forms.
- Rules are pattern transformations on expressions.
- At each step, the system scans for rule matches and rewrites matching subexpressions.
- Chapter 3 describes a left-to-right scan that applies transformations wherever possible without overlap.

Example rule shape:

- A pattern rule such as `e[x_][y_] -> x[x[y]]`, where pattern variables match subexpressions.

What makes this construction different:

- The state has hierarchical expression structure.
- Matching can be non-local relative to a one-dimensional cell lattice.
- A single rewrite can duplicate, delete, or rearrange whole subexpressions.
- The update rule is closer to symbolic algebra or term rewriting than to local cell evolution.

API shape:

- `expression`: initial symbolic tree.
- `rules`: one or more pattern rewrite rules.
- `scan_order`: for example left-to-right.
- `overlap_policy`: whether overlapping matches are disallowed.
- `step_policy`: apply first match, all non-overlapping matches, or another explicit convention.

## Higher-Dimensional, Network, Multiway, And Constraint Systems

The two-dimensions chapter extends the index in two directions. First, several earlier systems are generalized from one-dimensional lines to two- and three-dimensional spaces. Second, the chapter introduces systems whose underlying structure is not a fixed spatial array at all: networks, multiway systems, and constraint-defined systems.

| System | Core Data Structure | Main Construction Difference From Earlier Systems |
| --- | --- | --- |
| Two-dimensional cellular automata | Fixed two-dimensional grid of cells | A cell has neighbors in several spatial directions rather than just left/right. |
| Moore-neighborhood cellular automata | Fixed two-dimensional grid with diagonal neighbors | The local neighborhood includes eight surrounding cells. |
| Three-dimensional cellular automata | Fixed three-dimensional lattice of cells | Neighborhoods extend through face, edge, or corner adjacency in 3D. |
| Higher-dimensional lattice cellular automata | Fixed lattice in any dimension | The dimension and lattice type become explicit construction parameters. |
| Two-dimensional Turing machines | Two-dimensional tape/grid plus stateful head | The head moves in four grid directions rather than along a line. |
| Two-dimensional substitution systems | Grid of squares or tiles | Tiles are replaced by smaller tile blocks. |
| Geometric replacement systems | Geometric objects in the plane | Replacement uses transformations of shapes, not necessarily a rigid grid. |
| Neighbor-dependent two-dimensional substitution systems | Grid of symbols or tiles | Tile replacement can depend on neighboring tiles. |
| Network systems | Nodes with directed labeled connections | The connection graph itself evolves; layout is only visualization. |
| Multiway systems | Set of possible sequence states | All possible rewrites are kept, creating a branching state graph. |
| Local constraint systems | Cells plus constraints on neighborhoods | Patterns are defined by satisfaction conditions, not by stepwise evolution. |
| Template constraint systems | Grid plus allowed local templates | Every local neighborhood must match one of a finite set of templates. |
| Seeded template constraint systems | Template constraints plus required occurrence | A particular template must occur somewhere, breaking translation freedom. |

## 21. Two-Dimensional Cellular Automata

Construction:

- Fixed two-dimensional grid of cells.
- Chapter 5 primarily uses square grids with black/white cells.
- All cells update in parallel.
- A cell's next state depends on local neighbors around its grid position.
- The chapter's first examples use the four orthogonal neighbors: up, down, left, and right.
- Rules are often totalistic: the new state depends on the number or average of black neighbors, plus sometimes the current state of the center cell.

Coding convention from the chapter:

- For two-color totalistic square-grid rules using four neighbors plus the center cell, the binary digits of a code number specify outputs for cases ordered by the number of black neighbors and the center-cell state.

What makes this construction different:

- One-dimensional cellular automata have left/right neighborhoods.
- Two-dimensional cellular automata have spatial growth and shape as part of the state.
- The construction introduces grid geometry and boundary/rendering questions that do not arise in a single row.

API shape:

- `dimension`: `2`.
- `lattice`: square, triangular, hexagonal, or custom.
- `states`: usually `{0, 1}` in the chapter examples.
- `neighborhood`: orthogonal neighbors, diagonal-inclusive neighbors, or explicit offsets.
- `rule_form`: totalistic, outer-totalistic, or explicit neighborhood table.
- `initial_pattern`: single cell, row of cells, finite shape, or full grid.
- `boundary_policy`: infinite blank background, finite wraparound, fixed boundary, or other.

## 22. Moore-Neighborhood Cellular Automata

Construction:

- Fixed two-dimensional square grid.
- The neighborhood includes all eight surrounding cells, including diagonals.
- The center cell may also be included in the rule logic.
- Rules can be totalistic over the eight neighbors, with conditions such as "exactly three black neighbors."

Examples from the chapter:

- A rule where the center cell becomes black if either 3 or 5 of its 8 neighbors were black.
- A rule where the center cell becomes black when exactly 3 of its 8 neighbors are black.

What makes this construction different:

- The four-neighbor square-grid rule uses von Neumann adjacency.
- This construction uses Moore adjacency, adding diagonal influence.
- Diagonal influence changes the symmetry and geometry of possible growth.

API shape:

- `dimension`: `2`.
- `lattice`: square.
- `neighborhood`: eight surrounding offsets.
- `include_center`: whether the current center state is an input.
- `rule_form`: totalistic over neighbor count or explicit table.

## 23. Three-Dimensional Cellular Automata

Construction:

- Fixed three-dimensional lattice of cells.
- Chapter 5 uses cubic lattices as the main example.
- Each cell has a finite neighborhood in three-dimensional space.
- All cells update in parallel.
- Cells are usually black/white in the displayed examples.

Neighborhood variants from the chapter:

- Six face-sharing neighbors.
- Twenty-six neighbors sharing either a face, edge, or corner.

What makes this construction different:

- The lattice has volume rather than area.
- Neighbor choices include face-only adjacency or full surrounding-cube adjacency.
- Visualization requires slices, projections, rendered surfaces, or selected stages rather than a simple spacetime diagram.

API shape:

- `dimension`: `3`.
- `lattice`: cubic or custom 3D lattice.
- `neighborhood`: face-sharing, full 26-neighbor, or explicit offsets.
- `rule_form`: totalistic, outer-totalistic, or explicit table.
- `initial_pattern`: single cell, line, plane patch, finite solid, or custom set.
- `rendering`: slices, isosurfaces, projections, animation frames, or voxel render.

## 24. Higher-Dimensional Lattice Cellular Automata

Construction:

- Fixed lattice in dimension `d`.
- Each site has a state from a finite alphabet.
- A finite neighborhood is defined by offsets in the lattice.
- All sites update in parallel.
- The chapter explicitly notes that square, triangular, hexagonal, cubic, crystal-like, and nonrepetitive arrangements are possible.

What makes this construction different:

- Dimension and lattice geometry are no longer incidental; they are first-class parameters.
- Rules need not be restricted to one-dimensional left/right or two-dimensional square-grid neighborhoods.
- Symmetry groups of the lattice can be used to reduce rule spaces or define totalistic forms.

API shape:

- `dimension`: integer or named geometry.
- `lattice`: square, triangular, hexagonal, cubic, crystal, irregular, or custom graph.
- `state_space`: finite alphabet.
- `neighborhood_offsets`: explicit list or generated by radius/adjacency rule.
- `rule_form`: explicit, totalistic, outer-totalistic, isotropic, or custom.
- `initial_region`: finite seed embedded in the lattice.

## 25. Two-Dimensional Turing Machines

Construction:

- Two-dimensional grid of tape cells.
- A single active head occupies one grid location.
- The head has an internal state.
- The rule reads the current head state and the current cell color.
- The rule writes a new cell color, updates the head state, and moves the head in one of the grid directions.
- Chapter 5 uses four possible movement directions on the square grid.

What makes this construction different:

- One-dimensional Turing machines move left or right on a tape.
- Two-dimensional Turing machines move across a plane.
- The head path becomes a two-dimensional trajectory, and cells may be revisited from many directions.

API shape:

- `dimension`: `2`.
- `symbols`: tape alphabet.
- `head_states`: finite state set.
- `head_position`: `(x, y)`.
- `movement_set`: up, down, left, right, or custom offsets.
- `rule`: map from `{head_state, current_symbol}` to `{write_symbol, move, next_head_state}`.
- `blank_symbol`: default cell value.

## 26. Two-Dimensional Substitution Systems

Construction:

- State is a two-dimensional arrangement of tiles, often squares.
- At each step, each tile is replaced by a block of smaller tiles.
- The simplest examples replace one square with a fixed square block such as a 2 by 2 arrangement.
- Replacements are applied in parallel.

What makes this construction different:

- One-dimensional substitution systems replace symbols with strings.
- Two-dimensional substitution systems replace tiles with tile arrays.
- The replacement has geometry, orientation, and scale.

API shape:

- `tile_types`: symbols or colored tile states.
- `tile_geometry`: square, triangle, hexagon, or custom.
- `replacement_rule`: map from tile type to tile patch.
- `scale_factor`: subdivision factor or geometric transform.
- `orientation_policy`: preserve, rotate, reflect, or rule-controlled.
- `update`: parallel tile replacement.

## 27. Geometric Replacement And Fractal Systems

Construction:

- State is a collection of geometric objects in the plane, such as squares.
- At each step, every object is replaced by two or more transformed objects.
- Transformations can include scaling, translation, rotation, and reflection.
- Objects need not remain on a rigid grid.
- Objects may overlap unless the construction explicitly prevents it.

What makes this construction different:

- Grid substitution systems keep objects aligned to a lattice.
- Geometric replacement systems operate directly on shapes and transformations.
- "Neighbor" relations may be undefined or unstable because objects can appear anywhere in the plane.

API shape:

- `primitive_shape`: square, triangle, segment, polygon, or custom.
- `replacement_transforms`: list of similarity or affine transforms.
- `orientation_policy`: whether child transforms depend on parent orientation.
- `overlap_policy`: allow, merge, mask, count multiplicity, or reject.
- `rendering_depth`: number of replacement iterations.

## 28. Neighbor-Dependent Two-Dimensional Substitution Systems

Construction:

- State is a grid of elements or tiles.
- Tiles are replaced in parallel.
- The replacement for a tile can depend on neighboring tiles.
- Chapter 5 presents this as the two-dimensional analog of neighbor-dependent one-dimensional substitution systems.

What makes this construction different:

- Ordinary two-dimensional substitution systems replace each tile independently.
- Neighbor-dependent versions add local interaction between tiles.
- This requires a defined grid or adjacency relation, unlike free geometric fractal replacement.

API shape:

- `tile_types`: alphabet.
- `grid`: square or other lattice.
- `context`: neighborhood offsets used to choose replacements.
- `replacement_rule`: map from neighborhood pattern to tile patch.
- `boundary_policy`: padding, wrapping, dropping, or finite-domain handling.
- `update`: parallel contextual replacement.

## 29. Network Systems

Construction:

- State is a graph-like network of nodes and directed connections.
- Chapter 5 focuses on networks where every node has exactly two outgoing labeled connections, often called "above" and "below" in the diagrams.
- Rules reroute connections based on local network structure.
- Some rules can add new nodes by inserting them into existing connections.
- Some rules can disconnect the network; the chapter sometimes tracks only the component reachable from a chosen node.

What makes this construction different:

- There is no fixed spatial lattice.
- Node positions in drawings are not part of the system state.
- The evolving object is the connection pattern itself.
- Structures resembling one-, two-, or three-dimensional arrays can be encoded purely by connectivity.

API shape:

- `node_set`: nodes, possibly unlabeled up to isomorphism.
- `edge_labels`: labels such as `above` and `below`.
- `out_degree`: fixed or variable.
- `initial_network`: graph specification.
- `local_probe`: paths or neighborhoods used by the rule.
- `rewrite_rule`: reroute, insert node, delete node, split component, or relabel.
- `component_policy`: keep all components or track a distinguished component.
- `canonicalization`: graph isomorphism handling for comparisons.

## 30. Multiway Systems

Construction:

- State at each step is a set of possible states, not one state.
- Individual states are often sequences of symbols.
- Rules define replacements for elements or blocks in sequences.
- At each step, all possible replacements are applied.
- All distinct resulting states are kept.
- The complete evolution can be represented as a directed graph whose nodes are states and whose edges are rewrite events.

What makes this construction different:

- Sequential substitution chooses one replacement path.
- Multiway systems keep every possible replacement path.
- Time is no longer a single line of states; it branches into a state graph.

API shape:

- `state_representation`: string, sequence, expression, graph, or custom.
- `initial_states`: one or more starting states.
- `rewrite_rules`: possible replacements.
- `branch_policy`: all matches, all rules, deduplicate resulting states.
- `state_identity`: exact equality, canonical form, or quotient by symmetry.
- `step_limit`: depth of multiway expansion.
- `growth_control`: pruning, memoization, or maximum state count.
- `rendering`: layer diagram, causal/state graph, counts by step, or compressed graph.

## 31. Local Constraint Systems

Construction:

- State is not generated by an explicit time evolution.
- A configuration must satisfy specified local constraints.
- Chapter 5 first considers one-dimensional and two-dimensional black/white cell arrays.
- Constraints can specify local neighbor counts, such as each black cell having a certain number of black neighbors.
- A pattern is valid if every local neighborhood satisfies the constraint.

What makes this construction different:

- Rules do not say how to update from one step to the next.
- The system is defined implicitly by the set of configurations that satisfy constraints.
- Finding a valid configuration may require search, backtracking, or proof of impossibility.

API shape:

- `domain`: one-dimensional line, two-dimensional grid, finite torus, infinite grid approximation, or custom graph.
- `states`: cell colors or symbols.
- `constraint`: predicate on each local neighborhood.
- `neighborhood`: adjacent cells used by the constraint.
- `global_requirements`: optional requirements beyond local validity.
- `solver`: enumeration, SAT, backtracking, propagation, or custom search.

## 32. Template Constraint Systems

Construction:

- State is a grid of cells.
- A finite set of local templates is specified.
- Each local neighborhood in the final pattern must match one of the allowed templates.
- Chapter 5 discusses templates around each cell and later complete 3 by 3 blocks including diagonal neighbors.

Rule-space notes from the chapter:

- For one template scheme, there are `4,294,967,296` possible sets of templates.
- The chapter also considers 3 by 3 templates, where there are `512` possible black/white templates and selected subsets are allowed.

What makes this construction different:

- Neighbor-count constraints specify totals.
- Template constraints specify exact allowed local arrangements.
- Adjacent templates overlap, so satisfying one template constrains nearby templates.

API shape:

- `grid`: usually two-dimensional.
- `states`: finite alphabet.
- `template_shape`: cross neighborhood, 3 by 3 block, or custom mask.
- `allowed_templates`: finite set of local patterns.
- `matching_policy`: rotations/reflections allowed or exact orientation only.
- `solver`: local propagation, backtracking, SAT, finite-region search.

## 33. Seeded Template Constraint Systems

Construction:

- A template constraint system plus at least one required global occurrence.
- The local pattern around some site must match a specified seed template.
- The rest of the pattern must still satisfy the allowed-template constraint everywhere.

What makes this construction different:

- Plain template constraints may allow many translated, rotated, or repetitive solutions.
- Requiring a seed template introduces a distinguished location or event.
- The seed can force global structure even though the local constraints remain the same everywhere.

API shape:

- `allowed_templates`: local template set.
- `required_templates`: templates that must appear at least once.
- `anchor_policy`: fixed center, anywhere in grid, or multiple anchors.
- `solution_domain`: finite periodic grid, finite open region, or infinite-grid search.
- `solver`: constructive growth with backtracking, SAT, or proof search.

## Number-Based And Continuous Systems

The systems in the numbers chapter broaden the index from discrete symbolic programs to numerical systems. The key construction distinction is that the evolving state may be an integer, rational number, real number, sequence of numbers, mathematical function, continuous field, or differential equation rather than a fixed array of discrete cells.

| System | Core Data Structure | Main Construction Difference From Cellular Automata |
| --- | --- | --- |
| Arithmetic iteration systems | One integer, rational, or real number | A single number is repeatedly transformed by arithmetic operations. |
| Piecewise integer maps | One non-negative integer | The arithmetic update depends on a predicate such as parity. |
| Digit-reversal arithmetic systems | One integer plus a base representation | The rule directly transforms the digit sequence before arithmetic. |
| Recursive sequences | A growing indexed sequence of numbers | New terms are computed from earlier terms. |
| Variable-index recursive sequences | A growing indexed sequence with data-dependent references | Earlier terms are selected by values already in the sequence. |
| Number-theoretic filtering systems | A candidate set or sequence of integers | Rules select numbers by divisibility or other arithmetic predicates. |
| Mathematical-constant digit systems | A single exact number plus representation scheme | A simple definition generates a digit or continued-fraction sequence. |
| Function-combination systems | A mathematical function over a continuous variable | A curve is generated by combining functions such as sines. |
| Continued-fraction-driven substitution systems | Variable-length sequence plus external coefficient stream | The replacement rule can change from step to step according to continued-fraction terms. |
| Iterated maps | One real number in an interval | A fixed map repeatedly updates a continuous value. |
| Continuous cellular automata | Fixed cell line with continuous cell states | Cells have real-valued gray levels instead of discrete colors. |
| Partial differential equation systems | Continuous field over continuous space and time | Evolution is specified by derivatives rather than discrete steps. |

## 34. Arithmetic Iteration Systems

Construction:

- State is a single number.
- The number may be an integer, rational number, or real number.
- At each step, the same arithmetic operation is applied.
- The resulting sequence can be rendered either by numeric size or by digit sequence in a chosen base.

Examples from the chapter:

- Constant addition: `n -> n + c`.
- Constant multiplication: `n -> a n`.
- Rational multiplication: `x -> (p/q) x`.

What makes this construction different:

- There is no spatial lattice of cells.
- A single global arithmetic operation updates the whole state.
- When rendered as digits, effects such as carrying can make a digit depend on faraway digits, so the rule is not local in the cellular automaton sense.

API shape:

- `number_type`: integer, rational, fixed precision real, arbitrary precision real, or exact symbolic number.
- `initial_value`: starting number.
- `operation`: arithmetic update function.
- `steps`: number of iterations.
- `representation_base`: base used when rendering digit sequences.
- `rendering`: value plot, digit rows, fractional-part plot, or size/length plot.

## 35. Piecewise Integer Maps

Construction:

- State is a single integer, usually constrained to remain non-negative or positive.
- At each step, a predicate is evaluated on the current integer.
- The next integer is computed by one of several arithmetic formulas.
- The predicate may be parity, divisibility, residue class, or another integer property.

Examples from the chapter:

- `n -> If[EvenQ[n], 3 n/2, 3 (n + 1)/2]`.
- `n -> If[EvenQ[n], 5 n/2, (n + 1)/2]`.
- A related register-machine rule: `n -> If[EvenQ[n], 3 n/2, (3 n + 1)/2]`.

What makes this construction different:

- The rule is a branching arithmetic program over one integer.
- It resembles a register machine compressed into a scalar recurrence.
- The digit representation is useful for analysis, but the rule itself is stated arithmetically.

API shape:

- `initial_value`: starting integer.
- `branches`: ordered predicate/update cases.
- `integer_policy`: exact integer arithmetic; reject or handle non-integer outputs.
- `observables`: parity trace, digit rows, value plot, logarithmic size plot.

## 36. Digit-Reversal Arithmetic Systems

Construction:

- State is a single integer.
- A base is chosen for representing the integer as digits.
- At each step, the digit sequence is transformed, then interpreted back as a number.
- The transformed number is combined arithmetically with the original number.

Example from the chapter:

- Write the base-2 digits of the current number in reverse order, interpret the result as a number, then add it to the original number.

What makes this construction different:

- The rule explicitly depends on a positional representation.
- The update combines symbolic digit manipulation with arithmetic.
- Unlike ordinary arithmetic iteration, the construction cannot be specified without choosing a representation base.

API shape:

- `initial_value`: starting integer.
- `base`: digit base.
- `digit_transform`: reverse, rotate, complement, sort, or another digit operation.
- `combine`: arithmetic operation such as add transformed value to original.
- `leading_zero_policy`: preserve, drop, or explicitly pad.

## 37. Recursive Sequences

Construction:

- State is a growing sequence of numbers `f[1], f[2], ...`.
- Initial terms are specified.
- A recurrence rule computes each new term from earlier terms.
- In the simplest form, dependencies are fixed offsets such as `f[n-1]` or `f[n-2]`.

Examples from the chapter:

- Fixed-lag recurrences, including sequences like powers of two and Fibonacci-type sequences.
- Rules using only addition and subtraction can still be used once earlier terms are available.

What makes this construction different:

- The evolving state is not one value but the whole history of generated values.
- The update rule appends one new value rather than rewriting all existing values.
- Fixed-lag recurrences access earlier terms by fixed positions relative to `n`.

API shape:

- `initial_terms`: seed list.
- `index_origin`: first index, such as 1.
- `recurrence`: formula for `f[n]`.
- `dependency_policy`: fixed offsets only.
- `invalid_index_policy`: halt, reject rule, use defaults, or extend definitions.

## 38. Variable-Index Recursive Sequences

Construction:

- Same growing sequence structure as recursive sequences.
- The recurrence can refer to earlier terms using indices that depend on previous values.
- A term such as `f[n - f[n - 1]]` is allowed if the resulting index is valid.

What makes this construction different:

- The rule's dependency graph is data-dependent.
- A previous value can determine which earlier value is read next.
- The rule must define what happens if a computed index is zero, negative, or beyond the generated prefix.

API shape:

- `initial_terms`: seed list.
- `recurrence`: expression that may include computed indices.
- `index_guard`: rule for validating computed references.
- `invalid_index_policy`: halt, reject, or use a specified boundary value.
- `observables`: values, differences, digit-sequence relation, or fluctuation plot.

## 39. Number-Theoretic Filtering Systems

Construction:

- State is a set, list, or stream of candidate integers.
- At each stage, a predicate removes or selects integers.
- The predicate is based on number-theoretic properties such as divisibility, divisor counts, representation counts, or primality-related constraints.

Example from the chapter:

- The sieve of Eratosthenes: start with all integers, then remove numbers divisible by successive integers; the remaining numbers are primes.

Other sequence constructions mentioned:

- Number of divisors or related divisor properties.
- Number of ways to express `n` as a sum of four squares.
- Number of ways to express an even `n` as a sum of two primes.

What makes this construction different:

- The system is not necessarily a time evolution of one local state.
- It is a rule-based filtering or measurement process over the integers.
- The output is often a derived sequence rather than the successive states of a machine.

API shape:

- `domain`: integer range or infinite stream.
- `predicate`: divisibility, primality, representation count, or other arithmetic test.
- `stage_policy`: one-shot, sieve stages, or incremental stream.
- `output`: survivors, removed elements, counts, gaps, or cumulative statistics.

## 40. Mathematical-Constant Digit Systems

Construction:

- State is an exact mathematical constant or expression.
- A representation scheme is chosen.
- The system generates a sequence of digits, continued-fraction terms, or other representation coefficients.

Examples from the chapter:

- Digits of `pi` in base 10 and base 2.
- Repeating digit sequences for rational numbers such as `1/3`.
- Continued fraction terms for constants such as `pi`, `pi^2`, `Sinh[1]`, and `Tanh[1]`.
- Square roots have repetitive continued fractions; higher roots are presented as producing less regular terms.

What makes this construction different:

- There is often no stepwise dynamical update on a mutable state.
- The "system" is the expansion procedure for a precisely defined number.
- Different representations can expose different structural regularities.

API shape:

- `constant`: exact expression or named constant.
- `representation`: positional digits, continued fraction, or another expansion.
- `base`: required for positional digits.
- `term_count`: number of terms or digits to generate.
- `rendering`: digit row, walk plot, histogram, or coefficient sequence.

## 41. Function-Combination Systems

Construction:

- State is a mathematical function of a continuous variable.
- The function is built from a finite expression using standard functions and arithmetic operations.
- The output is a curve, zero-crossing sequence, or sampled representation.

Examples from the chapter:

- Sums of sine functions such as `Sin[x] + Sin[alpha x]`.
- Axis-crossing patterns for two sine or cosine terms.
- Curves related to the Riemann zeta function, such as the Riemann-Siegel Z function.

What makes this construction different:

- The object being studied is a continuous curve, not a discrete evolution rule.
- Some derived discrete sequences arise only after sampling, detecting crossings, or expanding a parameter such as a continued fraction.
- The rule is an expression tree defining a function.

API shape:

- `expression`: symbolic function definition.
- `domain`: interval of `x` values.
- `sampling_policy`: resolution or exact event detection.
- `derived_observables`: zero crossings, extrema, sign sequence, waveform samples.
- `parameter_representation`: optional continued-fraction or digit expansion for parameters.

## 42. Continued-Fraction-Driven Substitution Systems

Construction:

- State is a sequence of symbols, as in a substitution system.
- A parameter has a continued-fraction expansion.
- Terms from that continued fraction determine which substitution rule is used at each step.
- Chapter 4 describes this in connection with zero-crossing patterns of curves such as `Cos[x] - Cos[alpha x]`.

What makes this construction different:

- Ordinary substitution systems use the same replacement rule at every step.
- Here the rule schedule is driven by a numerical representation of a parameter.
- The system links a continuous function construction to a discrete symbolic evolution.

API shape:

- `symbols`: sequence alphabet.
- `initial_word`: starting sequence.
- `coefficient_source`: continued-fraction terms for a parameter.
- `rule_generator`: map from a coefficient to a substitution rule.
- `step_policy`: apply the generated rule for the current coefficient.
- `derived_from`: optional source function, such as a two-frequency sine or cosine expression.

## 43. Iterated Maps

Construction:

- State is a single real number, often constrained to an interval such as `[0, 1]`.
- A fixed map updates the value at every step.
- The map may be continuous, discontinuous, piecewise, or defined using operations such as fractional part.
- The same run can be studied by plotting values or by rendering digit sequences.

Examples from the chapter:

- `x -> FractionalPart[3/4 x]`.
- `x -> FractionalPart[2 x]`.
- `x -> If[x < 1/2, 3/2 x, 3/2 (1 - x)]`.
- `x -> FractionalPart[3/2 x]`.

What makes this construction different:

- It is a one-variable continuous-state dynamical system.
- Unlike integer maps, the state can contain infinitely many digits of information.
- Some maps act directly on digit representations, such as the shift map.

API shape:

- `interval`: allowed value range.
- `initial_value`: exact or approximate starting value.
- `map`: update function.
- `precision_policy`: exact, arbitrary precision, fixed precision, or interval arithmetic.
- `representation_base`: optional digit rendering base.
- `observables`: value plot, digit rows, sensitivity comparison.

## 44. Continuous Cellular Automata

Construction:

- Fixed one-dimensional lattice of cells.
- Each cell has a continuous gray level, usually in `[0, 1]`.
- All cells update in parallel.
- The local aggregate is usually the average of a cell and its immediate neighbors.
- A fixed map is applied to that aggregate to produce the next gray level.

Examples from the chapter:

- New gray level equals the average of the cell and its neighbors.
- New gray level is `FractionalPart[3/2 average]`.
- New gray level is `FractionalPart[average + c]`, with examples such as `c = 1/4`.

What makes this construction different:

- It keeps the fixed lattice, neighborhood, and parallel update of cellular automata.
- It replaces a finite state alphabet with continuous values.
- Its rule form combines totalistic cellular automata with iterated maps.

API shape:

- `dimension`: one-dimensional in the chapter examples.
- `value_range`: usually `[0, 1]`.
- `initial_field`: list/function for initial gray levels.
- `neighborhood`: usually radius-1.
- `aggregate`: average, weighted average, sum, or another local reducer.
- `map`: continuous update map applied after aggregation.
- `precision_policy`: numeric precision and rounding policy.

## 45. Partial Differential Equation Systems

Construction:

- State is a continuous field, such as gray level `u[t, x]`.
- Space and time are treated as continuous.
- The rule specifies rates of change using derivatives.
- The equation may involve derivatives with respect to time and space, plus nonlinear functions of the field.
- Initial conditions specify the field, and sometimes time derivatives, at the starting time.

Examples from the chapter:

- Diffusion equation: `partial_t u = 1/4 partial_xx u`.
- Wave equation: `partial_tt u = partial_xx u`.
- Sine-Gordon equation: `partial_tt u = partial_xx u + Sin[u]`.
- Nonlinear equations of the form `partial_tt u = partial_xx u + (1 - u^2)(1 + a u)`.

What makes this construction different:

- There are no discrete cells and no discrete time steps in the mathematical specification.
- Evolution is specified infinitesimally by differential relationships.
- Any computer experiment requires a numerical approximation scheme, so the solver and discretization become part of the experimental setup even if they are not part of the mathematical rule.

API shape:

- `field`: dependent variable, such as `u[t, x]`.
- `spatial_domain`: continuous interval or boundary conditions.
- `time_domain`: time interval.
- `equation`: differential equation or system of equations.
- `initial_conditions`: values and required derivatives at initial time.
- `boundary_conditions`: fixed, periodic, open, or infinite-domain approximation.
- `solver`: numerical method and discretization parameters.
- `validation_policy`: checks for blowup, stiffness, resolution artifacts, and conservation laws when applicable.

## Practical Takeaway For A Simple-Program API

A construction-first API should model each adjacent system as a different engine with explicit structural parameters. The important design choice is to keep the rule, state representation, update schedule, and initial condition separate.

Shared top-level fields:

- `system_type`: `cellular_automaton`, `mobile_automaton`, `turing_machine`, `substitution_system`, `tag_system`, `register_machine`, `symbolic_system`, `network_system`, `multiway_system`, `constraint_system`, `arithmetic_iteration`, `integer_map`, `recursive_sequence`, `number_filter`, `generalized_substitution_system`, `iterated_map`, `continuous_cellular_automaton`, or `partial_differential_equation`.
- `alphabet`, `states`, or `value_space`: symbols, colors, head states, expression atoms, graph nodes, integers, real intervals, or continuous fields.
- `initial_condition`: seed state, initial string, blank tape plus head state, register values, symbolic expression, graph, number, sequence prefix, template seed, or field profile.
- `rule`: exact transition table, replacement list, instruction list, rewrite rule set, graph rewrite, constraint predicate, template set, map, or equation.
- `step_policy`: parallel, single-active-cell, first-match, cyclic, instruction-pointer, all-non-overlapping rewrites, all-possible rewrites, graph rewrite, constraint solving, arithmetic iteration, recurrence append, map iteration, or continuous-time solver.
- `boundary_policy`: blank padding, dropping, wrapping, unbounded tape, finite torus, open region, infinite-grid approximation, or explicit halting.
- `rendering`: spacetime diagram, grid snapshots, voxel view, compressed event view, expression tree view, network graph, multiway graph, register trace, length/growth plot, digit rows, value plot, waveform, or field plot.

Engine-specific fields:

- Cellular automata: `dimension`, `neighborhood`, `rule_form`, `background_state`, `symmetries`.
- Mobile automata: `active_position`, `read_window`, `write_window`, `move_set`.
- Generalized mobile automata: `active_set`, `activity_rule`, `write_conflict_policy`.
- Turing machines: `tape_symbols`, `head_states`, `blank_symbol`, `head_position`, `movement_set`.
- Substitution systems: `replacement_scope`, `context`, `parallel_replacement`, `tile_geometry`, `scale_factor`.
- Sequential substitution systems: `replacements`, `scan_direction`, `match_policy`.
- Tag systems: `deletion_number`, `append_rule`, `halt_policy`.
- Cyclic tag systems: `program`, `program_counter`, `trigger_symbol`.
- Register machines: `registers`, `instructions`, `instruction_pointer`, `zero_policy`.
- Symbolic systems: `expression`, `pattern_language`, `scan_order`, `overlap_policy`.
- Geometric replacement systems: `primitive_shape`, `replacement_transforms`, `orientation_policy`, `overlap_policy`.
- Network systems: `node_set`, `edge_labels`, `out_degree`, `local_probe`, `rewrite_rule`, `canonicalization`.
- Multiway systems: `initial_states`, `rewrite_rules`, `branch_policy`, `state_identity`, `growth_control`.
- Constraint systems: `domain`, `constraint`, `template_shape`, `allowed_templates`, `required_templates`, `solver`.
- Arithmetic iteration and integer maps: `number_type`, `operation`, `branches`, `representation_base`, `integer_policy`.
- Recursive sequences: `initial_terms`, `recurrence`, `dependency_policy`, `invalid_index_policy`.
- Number-theoretic filters: `domain`, `predicate`, `stage_policy`, `output`.
- Mathematical constants: `constant`, `representation`, `base`, `term_count`.
- Function combinations: `expression`, `domain`, `sampling_policy`, `derived_observables`.
- Continued-fraction-driven substitution systems: `coefficient_source`, `rule_generator`, `initial_word`, `derived_from`.
- Iterated maps: `interval`, `map`, `precision_policy`, `representation_base`.
- Continuous cellular automata: `value_range`, `aggregate`, `map`, `precision_policy`.
- Partial differential equations: `field`, `equation`, `initial_conditions`, `boundary_conditions`, `solver`.

This separation avoids confusing construction classes with emergent behavior classes, and it also makes it possible to compare systems that look very different while preserving the exact semantics of each one.

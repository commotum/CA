"""Template for component catalog and pipeline scaffolds.

This file is a reference shape for new `data/components/*.py` catalogs. It is
not a runtime component. The goal is to make future scaffolds look and read like
`alphabets.py`, `neighborhoods.py`, `frontiers.py`, and `rules.py` without
needing to rediscover the project style.

Use this structure when adding a new component catalog:

- Start with a clear module docstring.
  - Say what semantic layer the module owns.
  - Say what the module explicitly does not own.
  - Name the lower-level modules it builds from.
  - Name the downstream modules that will consume its output.
- Keep one frozen dataclass for the primary structured artifact when possible.
  - Store the real payload first.
  - Store `family`, `name`, `params`, and `metadata` only when they help rebuild
    or inspect the artifact.
  - Avoid dataclasses for tiny transforms when a simple factory function is
    clearer.
- Keep the scaffold phase-ordered.
  - Phase 1 singular primitives come before Phase 1 compounds.
  - Later general families and aliases stay visibly later.
- Leave unimplemented phases as docstring-rich stubs.
  - Do not half-implement future phases.
  - Do not add clever placeholder behavior.
  - Use `_not_implemented()` so all unfinished catalog entries fail the same
    way.

Implementation style once a stub is ready:

- Prefer extremely skimmable code over dense code.
- Validate arguments early and return early when the branch is done.
- Normalize input values near the top of the function.
- Use the project primitives instead of reimplementing lower-level behavior.
- Build compound families by composing named singular families.
- Keep comments short and only where they explain a non-obvious decision.
- Preserve user edits and unrelated work; keep each implementation scoped to
  the requested phase.

For top-level pipeline modules, use the same ownership-first shape:

- `prepare.py` freezes deterministic source manifests, stream specs, and vocab
  recipes.
- `data/generate.py` rolls one already chosen seed state forward.
- `data/tokenize.py` builds vocabularies and serializes one realized episode.
- `data/batch.py` realizes train/eval streams, filters rollouts at runtime, and
  builds tensors.

Those modules should start with a big-picture docstring, define a small public
stub surface below it, and leave compatibility or migrated legacy code clearly
below the new scaffold until the implementation catches up.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from typing import Any, Literal


CombineMode = Literal["tuple", "merge"]


@dataclass(frozen=True)
class Component:
    """Structured artifact produced by this catalog.

    Replace `items` with the real payload for the component. Examples from
    existing catalogs are neighborhood selectors, frontier selectors, alphabet
    values, or rule channels.

    Keep the fields boring and inspectable:

    - `items`: the payload consumed by downstream code.
    - `combine`: explicit composition semantics when the artifact has parts.
    - `family`: the factory family that produced the artifact.
    - `params`: normalized parameters needed to rebuild the artifact.
    - `name`: optional human-readable label for named families.

    Do not add fields just because they might be useful later. Add them when a
    real downstream consumer needs them.
    """

    items: tuple[Any, ...]
    combine: CombineMode = "tuple"
    family: str | None = None
    params: Mapping[str, Any] | None = None
    name: str | None = None


def _not_implemented() -> None:
    """Raise the standard catalog-stub error.

    Every unfinished scaffold function should call this. Keeping a single
    helper makes placeholder behavior obvious and easy to find.
    """

    raise NotImplementedError("scaffold.py is a component catalog template")


# ---------------------------------------------------------------------------
# Phase 1.1 Singular Primitives
# ---------------------------------------------------------------------------


def singular_primitive(value: int = 0) -> Component:
    """Build the smallest meaningful artifact owned by this catalog.

    Singular primitives should be built directly from the lower-level module
    this catalog depends on. For example, `neighborhoods.py` builds singular
    read loci from `loci.py`; it does not ask `datasets.py` or `generate.py` to
    help.

    Implementation checklist:

    - Normalize inputs first.
    - Validate obvious invalid values before doing work.
    - Build exactly one coherent component.
    - Return a `Component` with normalized `params`.
    """

    _not_implemented()


# ---------------------------------------------------------------------------
# Phase 1.2 Compound Families
# ---------------------------------------------------------------------------


def named_compound(value: int = 0) -> Component:
    """Build a named compound from singular primitives.

    Compound families should compose existing named families. They should not
    duplicate the lower-level construction used by their parts.

    A good compound reads like this:

    ```text
    primitive_a(...)
    primitive_b(...)
    compose((a, b))
    ```

    The final returned object should preserve the semantic name and the
    normalized parameters for the named family.
    """

    _not_implemented()


def compose(
    components: Sequence[Component],
    combine: CombineMode = "tuple",
) -> Component:
    """Compose singular or already-structured components.

    Keep composition explicit. If component boundaries matter downstream, use a
    tuple-preserving mode. If a future catalog intentionally flattens support,
    make that choice visible through `combine`.

    Implementation checklist:

    - Validate `combine`.
    - Reject empty component lists.
    - Flatten only the payload level that this catalog owns.
    - Return a new structured object rather than mutating inputs.
    """

    _not_implemented()

# ---------------------------------------------------------------------------
# Phase 2 General Families
# ---------------------------------------------------------------------------


def general_family(values: Sequence[int]) -> Component:
    """Build a broader family after Phase 1 behavior is stable.

    Phase 2 functions are for reusable generalizations, not one-off experiment
    shortcuts. If the function is only an alias over an existing primitive,
    place it in Phase 3 instead.
    """

    _not_implemented()


# ---------------------------------------------------------------------------
# Phase 3 Aliases
# ---------------------------------------------------------------------------


def alias_family(value: int = 0) -> Component:
    """Alias for a clearer or more domain-specific family name.

    Aliases should delegate to existing primitives or general families. They
    should not introduce separate construction logic.
    """

    _not_implemented()

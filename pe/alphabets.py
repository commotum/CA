"""Alphabet and value-space catalog factories.

Treat this as a tentative plan, not a prescription.

This module defines raw value spaces used by generated datasets. An alphabet is
not a vocabulary and does not assign token ids. It only defines the values a
trajectory cell, symbol, register, or field may contain before tokenization or
numerical handling.

Token ids are assigned later by `data/tokenize.py`, which enumerates special
tokens first and then adds the alphabets required by the selected dataset
configs. This keeps alphabet definitions reusable and prevents fixed global
vocabulary constants from creeping into the component layer.

Prefer parameterized alphabet families over named constants. Scalar numerical
values use range alphabets, while binary cellular automata use the boolean
alphabet:

```text
int_range_alphabet(size=97)
float_range_alphabet(size=5, start=0.0, step=0.25)
boolean()
```

If a rule needs modular arithmetic, that modular behavior belongs in the rule
specification. The alphabet only needs to say which values are legal.

Likewise, totalistic behavior, ordered-neighborhood behavior, blank/quiescent
backgrounds, digit-base interpretation, tape-symbol roles, and head-state roles
belong to rules, engines, encodings, or dataset metadata. They should not become
new primitive alphabet families unless they change the underlying value-space
semantics.
"""

from __future__ import annotations

import math
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from typing import Any, Hashable, Literal


Value = int | float | str


@dataclass(frozen=True)
class Alphabet:
    """Finite set of raw trajectory values.

    `values` stores the legal cell values in deterministic order. `family` and
    `params` preserve the catalog recipe that produced the alphabet so configs
    can be compared, deduplicated, and rebuilt without relying on hard-coded
    constants.
    """

    values: tuple[Value, ...]
    family: str
    params: Mapping[str, Any]
    name: str | None = None


@dataclass(frozen=True)
class IntegerSpace:
    """Discrete integer value space.

    This is for future number-based engines such as register machines, integer
    maps, arithmetic iterations, and recursive sequences. It is not directly a
    finite token alphabet unless `upper` and `lower` make the range finite or a
    tokenizer/discretizer explicitly bounds it.
    """

    lower: int | None = None
    upper: int | None = None
    family: str = "integer_space"
    params: Mapping[str, Any] | None = None
    name: str | None = None


@dataclass(frozen=True)
class RealInterval:
    """Continuous scalar interval value space.

    This is for future continuous cellular automata and iterated maps. It is not
    directly tokenizable without a discretization, quantization, or regression
    target policy in the tokenizer/model layer.
    """

    low: float = 0.0
    high: float = 1.0
    closed: bool = True
    family: str = "real_interval"
    params: Mapping[str, Any] | None = None
    name: str | None = None


ValueSpace = Alphabet | IntegerSpace | RealInterval


def _not_implemented() -> None:
    raise NotImplementedError("alphabets.py currently contains catalog specs only")


# ---------------------------------------------------------------------------
# Core Alphabet Families
# ---------------------------------------------------------------------------


def int_range_alphabet(size: int, start: int = 0) -> Alphabet:
    """Build a contiguous integer alphabet.

    This is the default family for scalar numerical recurrences and other
    numeric value spaces. `int_range_alphabet(size=97)` represents values
    `{0, ..., 96}`.

    This family should be preferred over named constants whenever a simple
    finite integer range is the semantic value space.
    """

    if isinstance(size, bool) or not isinstance(size, int):
        raise TypeError(f"size must be an integer, got {type(size).__name__}")

    if isinstance(start, bool) or not isinstance(start, int):
        raise TypeError(f"start must be an integer, got {type(start).__name__}")

    if size <= 0:
        raise ValueError(f"size must be positive, got {size}")

    values = tuple(range(start, start + size))

    return Alphabet(
        values=values,
        family="int_range_alphabet",
        params={"size": size, "start": start},
    )


def float_range_alphabet(size: int, start: float = 0.0, step: float = 1.0) -> Alphabet:
    """Build a finite evenly spaced float-valued alphabet.

    This is for discretized real scalar values, not continuous intervals.
    `float_range_alphabet(size=5, start=0.0, step=0.25)` represents
    `{0.0, 0.25, 0.5, 0.75, 1.0}`.
    """

    if isinstance(size, bool) or not isinstance(size, int):
        raise TypeError(f"size must be an integer, got {type(size).__name__}")

    if isinstance(start, bool) or not isinstance(start, (int, float)):
        raise TypeError(f"start must be an int or float, got {type(start).__name__}")

    if isinstance(step, bool) or not isinstance(step, (int, float)):
        raise TypeError(f"step must be an int or float, got {type(step).__name__}")

    if size <= 0:
        raise ValueError(f"size must be positive, got {size}")

    start = float(start)
    step = float(step)

    if not math.isfinite(start):
        raise ValueError(f"start must be finite, got {start}")

    if not math.isfinite(step):
        raise ValueError(f"step must be finite, got {step}")

    if step == 0.0:
        raise ValueError("step cannot be zero")

    values = tuple(start + index * step for index in range(size))

    return Alphabet(
        values=values,
        family="float_range_alphabet",
        params={"size": size, "start": start, "step": step},
    )


def boolean() -> Alphabet:
    """Build the canonical two-state boolean alphabet.

    The raw values are still `0` and `1`, but the family records that these are
    boolean off/on states rather than scalar numerical values. Tokenization can
    therefore share boolean tokens across CA datasets without merging them with
    numeric range alphabets that happen to contain the same integers.
    """

    return Alphabet(
        values=(0, 1),
        family="boolean",
        params={},
    )


def symbolic(values: Sequence[Hashable]) -> Alphabet:
    """Build an alphabet from explicit symbolic values.

    This is reserved for non-numeric or semantically named cell states. Values
    should remain finite, deterministic, and directly tokenizable.
    """

    values = tuple(values)

    if not values:
        raise ValueError("values cannot be empty")

    seen = set()
    for value in values:
        if isinstance(value, bool):
            raise TypeError("symbolic values must be int or str, not bool")

        if not isinstance(value, (int, str)):
            raise TypeError(
                f"symbolic values must be int or str, got {type(value).__name__}"
            )

        if value in seen:
            raise ValueError(f"symbolic values must be unique, duplicate {value!r}")

        seen.add(value)

    return Alphabet(
        values=values,
        family="symbolic",
        params={"values": values},
    )


# ---------------------------------------------------------------------------
# Phase 2 Future Value-Space Families
# ---------------------------------------------------------------------------


def composite(
    layers: Mapping[str, Alphabet | Mapping[str, Any]],
    mode: Literal["product", "tagged_union"] = "product",
) -> Alphabet:
    """Build a finite composite alphabet from finite layers.

    This is the future hook for systems whose cell value carries multiple
    finite roles, such as a tape symbol plus an optional head state, or a color
    layer plus an activity marker. `mode="product"` enumerates combinations of
    layer values. `mode="tagged_union"` enumerates tagged alternatives.

    This should only be used when the composite value itself is the raw cell
    value. Engine-level roles such as `blank_symbol`, `head_state`, or
    `active_position` should remain engine metadata when they are not stored in
    every cell.
    """

    _not_implemented()


def integer_space(lower: int | None = 0, upper: int | None = None) -> IntegerSpace:
    """Build an integer value space for future number-based systems.

    This covers register values, integer maps, arithmetic iterations, and
    integer recursive sequences. Unbounded integer spaces are value spaces, not
    finite alphabets. A tokenizer must either reject them, bound them, or use a
    separate numeric representation policy.
    """

    _not_implemented()


def real_interval(low: float = 0.0, high: float = 1.0, closed: bool = True) -> RealInterval:
    """Build a continuous scalar interval for future continuous systems.

    This covers continuous cellular automata and iterated maps whose state value
    is a real scalar, usually in `[0, 1]`. It requires a downstream numerical or
    discretization policy before it can participate in tokenized training.
    """

    _not_implemented()

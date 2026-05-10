"""Alphabet and value-space catalog factories.

This module defines raw value spaces used by generated trajectories. An
alphabet is not a vocabulary and does not assign token ids. It only defines the
values a trajectory cell, symbol, register, or field may contain before
downstream representation or numerical handling.

Any representation ids are assigned later by downstream code. This keeps
alphabet definitions reusable and prevents fixed global vocabulary
constants from creeping into the CA layer.

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
belong to rules, engines, encodings, or system metadata. They should not become
new primitive alphabet families unless they change the underlying value-space
semantics.
"""

from __future__ import annotations

import math
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from typing import Any


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
    boolean off/on states rather than scalar numerical values. Downstream
    representation can therefore treat boolean states consistently without
    merging them with numeric range alphabets that happen to contain the same
    integers.
    """

    return Alphabet(
        values=(0, 1),
        family="boolean",
        params={},
    )


def symbolic(values: Sequence[int | str]) -> Alphabet:
    """Build an alphabet from explicit symbolic values.

    This is reserved for non-numeric or semantically named cell states. Values
    should remain finite, deterministic, and directly representable.
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

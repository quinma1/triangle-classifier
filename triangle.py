"""Triangle classifier."""

import math

REL_TOL = 1e-9
ABS_TOL = 1e-12


def _close(x, y):
    return math.isclose(x, y, rel_tol=REL_TOL, abs_tol=ABS_TOL)


def _is_number(x):
    # bool is a subclass of int; reject it so True/False aren't treated as 1/0
    return isinstance(x, (int, float)) and not isinstance(x, bool)


def is_valid_triangle(a, b, c) -> bool:
    sides = (a, b, c)
    if not all(_is_number(s) for s in sides):
        return False
    if not all(math.isfinite(s) for s in sides):
        return False
    if any(s <= 0 for s in sides):
        return False
    x, y, z = sorted(sides)
    # Degenerate case (x + y == z) is invalid; use a tolerance so float
    # rounding (e.g. 0.1 + 0.2 vs 0.3) can't sneak a flat triangle through.
    return x + y > z and not _close(x + y, z)


def classify_triangle(a, b, c) -> str:
    if not is_valid_triangle(a, b, c):
        return "Invalid"

    x, y, z = sorted((a, b, c))

    if _close(x, y) and _close(y, z):
        kind = "Equilateral"
    elif _close(x, y) or _close(y, z) or _close(x, z):
        kind = "Isosceles"
    else:
        kind = "Scalene"

    if _close(x * x + y * y, z * z):
        return "Right " + kind
    return kind

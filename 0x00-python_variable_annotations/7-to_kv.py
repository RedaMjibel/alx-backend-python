#!/usr/bin/env python3
"""
A type annotated function
"""


def to_kv(k: str, v: int | float) -> Tuple[str, float]:
    """Return a tuple containing k and the square of v."""
    return k, float(v) ** 2

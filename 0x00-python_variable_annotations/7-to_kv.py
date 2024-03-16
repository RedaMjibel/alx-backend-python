#!/usr/bin/env python3
"""
A type annotated function
"""

from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple containing k and the square of v."""
    return (k, v**2)

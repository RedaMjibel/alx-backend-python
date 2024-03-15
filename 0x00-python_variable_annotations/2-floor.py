#!/usr/bin/env python3
"""
Basic annotations - floor
"""


def floor(n: float) -> int:
    """ Returns floor of number """
    return int(n) if n >= 0 else int(n) - 1

#!/usr/bin/env python3
"""
Module make multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by multiplier.
    """
    def wrapper(n: float) -> float:
        """
        Multiplies n by multiplier
        """
        return multiplier * n
    return wrapper

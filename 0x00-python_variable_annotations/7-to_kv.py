#!/usr/bin/env python3
"""
Module to kv
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tupl of string and float
    """
    return (k, float(v ** 2))

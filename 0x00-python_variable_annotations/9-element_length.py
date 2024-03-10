#!/usr/bin/env python3
"""
Module Duck
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns Iterable
    """
    return [(i, len(i)) for i in lst]

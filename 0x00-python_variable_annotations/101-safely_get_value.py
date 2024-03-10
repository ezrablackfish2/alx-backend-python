#!/usr/bin/env python3
"""
Module More involved type annotations
"""
from typing import Any, Mapping, Optional, TypeVar, Union
T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Optional[T] = None) -> Union[Any, T]:
    """
    Return value with a key @key or default
    """
    if key in dct:
        return dct[key]

    return default

#!/usr/bin/env python3
"""
Module concurrent coroutines
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Returns list of all delays
    """
    t = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = []
    for res in asyncio.as_completed(t):
        delay = await res
        delays.append(delay)

    return delays

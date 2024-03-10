#!/usr/bin/env python3
"""
Module measure runtime
"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Execute async_comprehension four times in parallel using asyncio.gather.
    and measure the total runtime and return it.
    """
    start = time.time()
    result = await asyncio.gather(*[async_comprehension() for _ in range(4)])
    return time.time() - start

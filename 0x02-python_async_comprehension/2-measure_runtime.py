#!/usr/bin/env python3
"""execute async_comprehension four times in parallel using asyncio.gather.
"""

import time
import asyncio
async_comprehension = __import__('1-async_comprehension.py').async_comprehension


async def measure_runtime() -> float:
    """measure time"""
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    end_time = time.time()
    return end_time - start_time

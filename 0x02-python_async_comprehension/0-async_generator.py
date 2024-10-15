#!/usr/bin/env python3
"""an async generator"""

import asyncio
import random


async def async_generator():
    """async generator"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

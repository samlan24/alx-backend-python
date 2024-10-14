#!/usr/bin/env python3
"""asyncio module"""

import asyncio
import random


async def wait_random(max_delay: int) -> float:
    """delays for a max delay_max seconds and then returns the delay"""
    delay = random.randint(0, max_delay)
    await asyncio.sleep(delay)
    return delay

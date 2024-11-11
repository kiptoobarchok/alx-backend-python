#!/usr/bin/env python3
"""
This module provides an asynchronous generator that yields random numbers.
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Coroutine that yields a random number between 0 and 10, 10 times,
    waiting 1 second asynchronously between each yield.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

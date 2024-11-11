#!/usr/bin/env python3
"""
A function that takes an integer max_delay and returns a asyncio.Task.
"""

import asyncio
from typing import Coroutine

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asynchronous task for wait_random.

    Args:
        max_delay (int): Maximum delay parameter for wait_random coroutine.

    Returns:
        asyncio.Task: asyncio Task object representing
        the execution of wait_random.
    """
    async def wrapper():
        return await wait_random(max_delay)

    return asyncio.create_task(wrapper())

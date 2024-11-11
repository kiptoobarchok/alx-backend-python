#!/usr/bin/env python3
'''
This module contains an asynchronous coroutine that waits for a random delay.
'''
import asyncio
from typing import List

# Import the wait_random function from 0-basic_async_syntax module
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''Executes wait_random n times.

    Args:
        n (int): The number of times to execute wait_random.
        max_delay (int): The maximum delay for wait_random.

    Returns:
        List[float]: A list of all the delays in ascending order.
    '''
    # Gather all wait_random coroutines and run them concurrently
    wait_times = await asyncio.gather(
        *tuple(map(lambda _: wait_random(max_delay), range(n)))
    )
    # Return the sorted list of wait times
    return sorted(wait_times)

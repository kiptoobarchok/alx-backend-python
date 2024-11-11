#!/usr/bin/env python3
'''
This module contains a function to measure the runtime of wait_n.
'''
import asyncio
import time

# Import the wait_n function from 1-concurrent_coroutines module
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''
    Measure the average runtime of the wait_n coroutine.

    Args:
        n (int): The number of times to execute the wait_n coroutine.
        max_delay (int): The maximum delay in seconds
        for each execution of wait_n.

    Returns:
        float: The average runtime per call of the wait_n coroutine.
    '''
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - start_time) / n

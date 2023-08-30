#!/usr/bin/env python3
""" commented module """


import time
wait_random = __import__('0-basic_async_syntax').wait_random


async def measure_time(n: int, max_delay: int) -> float:
    """Measure total execution time for wait_n(n, max_delay)"""
    start_time = time.time()


    await wait_n(n, max_delay)

    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n

#!/usr/bin/env python3
""" commented module """


import time
wait_random = __import__('0-basic_async_syntax').wait_random


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the average execution time for the `wait_n` function.

    Args:
        n (int): The number of times to call `wait_n`.
        max_delay (int): The maximum delay in seconds for each `wait_n` call.

    Returns:
        float: The average execution time per call in seconds.
    """

    async def async_measure():
        """
        An asynchronous function that measures the execution time of `wait_n`.

        Returns:
            float: The execution time in seconds for a single `wait_n` call.
        """
        start = time.time()
        await wait_n(n, max_delay)
        end = time.time()
        return (end - start) / n

    return asyncio.run(async_measure())

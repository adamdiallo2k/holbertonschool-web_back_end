#!/usr/bin/env python3
"""measures the total execution time for wait_n"""


import random
import asyncio
from typing import Union
wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous routine that spawns task_wait_random n times with the
    specified max_delay.

    Args:
        n (int): The number of times to spawn task_wait_random.
        max_delay (int): The maximum delay in seconds for each
        task_wait_random call.

    Returns:
        List[float]: A list of delays (float values)
        in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)

    sorted_delays = sorted(delays)
    return sorted_delays

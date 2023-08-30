#!/usr/bin/env python3
"""measures the total execution time for wait_n"""


import random
import asyncio
from typing import Union
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Return an asyncio Task"""
    return asyncio.create_task(wait_random(max_delay))

async def task_wait_n(n: int, max_delay: int):
    """Use task_wait_random to create multiple asyncio Tasks"""
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]

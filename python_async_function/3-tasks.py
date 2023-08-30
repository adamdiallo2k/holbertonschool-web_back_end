#!/usr/bin/env python3
"""measures the total execution time for wait_n"""


import random
import asyncio
from typing import Union
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Return an asyncio Task"""
    return asyncio.create_task(wait_random(max_delay))

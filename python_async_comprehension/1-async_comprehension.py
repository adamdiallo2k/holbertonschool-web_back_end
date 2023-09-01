#!/usr/bin/env python3
""" commented modue """


import asyncio
import random
From Typing import List
async_generator = __import__('0-async_generator').async_generator

async def async_comprehension() -> List[float]:
    """ commented function """
    return [number async for number in async_generator()]
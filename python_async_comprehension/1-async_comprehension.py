#!/usr/bin/env python3
""" commented modue """


import asyncio
import random
async_generator = __import__('0-async_generator.py').async_generator

async def async_comprehension():
    """ commented function """
    return [number async for number in async_generator()]
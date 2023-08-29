#!/usr/bin/env python3
""" commented module """

import random, asyncio
from typing import Union


async def wait_random(max_delay: Union[int, float] = 10) -> float:
    """ commented function """
    await asyncio.sleep(1)
    return random.uniform(0, float(max_delay))

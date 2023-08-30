#!/usr/bin/env python3
""" commented module """


import wait_random
from typing import List

async def wait_n(n: int, max_delay: int) -> List[float]:
    """  return the list of all the delays (float values) """
    listfloat = []
    for _ in range(n):
        delay = await wait_random(max_delay)
        listfloat.append(delay)
    listfloat.sort()
    return listfloat
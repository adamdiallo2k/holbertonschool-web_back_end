#!/usr/bin/env python3
""" commented module """


from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random
from typing import List


async def wait_n(n: int, max_delay: int) -> List[float]:
    """  return the list of all the delays (float values) """
    listfloat = []
    for _ in range(n):
        delay = await wait_random(max_delay)
        listfloat.append(delay)
    return sorted(listfloat)

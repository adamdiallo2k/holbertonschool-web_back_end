from 0_basic_async_syntax import wait_random
from typing import List

async def wait_n(n: int, max_delay: int) -> List[float]:
    listfloat = []
    for _ in range(n):
        delay = await wait_random(max_delay)
        listfloat.append(delay)
    listfloat.sort()
    return listfloat

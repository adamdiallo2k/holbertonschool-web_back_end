#!/usr/bin/env python3
""" commented module """


import time
wait_random = __import__('0-basic_async_syntax').wait_random


async def measure_time(n: int, max_delay: int) -> float:
    """ commented function """
    start_time = time.time()
    n = wait_random(2,3)
    end_time = time.time()
    Total_time = end_time - start_time
    Total_time = Total_time / n
    return float(Total_time)

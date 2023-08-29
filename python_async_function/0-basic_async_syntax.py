#!/usr/bin/env python3
""" commented module """

import random, asyncio
import Union


def wait_random(max_delay = 10):
    """ commented function """
    await asyncio.sleep(1)
    return random.randint(0, max_delay)

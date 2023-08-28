#!/usr/bin/env python3
""" commented module """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ commented function """
    def multiplier_function(x: float) -> float:
        """ commented function """
        return x * multiplier
    return multiplier_function

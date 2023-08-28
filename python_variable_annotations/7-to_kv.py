#!/usr/bin/env python3
""" commented module """
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ commented function """
    return (k, float(v**2))

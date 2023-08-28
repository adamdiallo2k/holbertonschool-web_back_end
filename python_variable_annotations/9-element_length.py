#!/usr/bin/env python3
""" commented module """


from typing import List, Tuple

def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """ commented function """
    return [(i, len(i)) for i in lst]
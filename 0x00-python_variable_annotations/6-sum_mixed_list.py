#!/usr/bin/env python3
"""returns sum of ints and floats"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """returns sum of ints and floats"""
    return sum(mxd_lst)

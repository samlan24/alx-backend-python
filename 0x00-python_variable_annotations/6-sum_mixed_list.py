#!/usr/bin/env python3
"""returns sum of ints and floats"""

from typing import List, Union


def sum_list(input_list: List[Union[int, float]]) -> float:
    """returns sum of ints and floats"""
    return sum(input_list)

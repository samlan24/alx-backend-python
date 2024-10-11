#!/usr/bin/env python3
""" returns a tuple"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """returns a tuple with k as the first value
    and v squared
    """
    return (k, float(v**2))

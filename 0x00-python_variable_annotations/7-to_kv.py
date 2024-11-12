#!/usr/bin/env python3

"""
7-to_kv.py

This module provides a function to create
a tuple with a string and the square of a number.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Creates a tuple with a string and the square of a number.

    Parameters:
    k (str): The string to be included in the tuple.
    v (Union[int, float]): The number to be squared and included in the tuple.

    Returns:
    Tuple[str, float]: A tuple where the first element is the string k,
    and the second element is the square of the number v as a float.
    """
    return (k, float(v ** 2))

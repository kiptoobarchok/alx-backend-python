#!/usr/bin/env python3

"""
6-sum_mixed_list.py

This module provides a function to sum a list of integers and floats.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sums a list of integers and floats and returns the result as a float.

    Parameters:
    mxd_lst (List[Union[int, float]]): List of integers & float numbers to sum.

    Returns:
    float: The sum of the numbers.
    """
    return sum(mxd_lst)

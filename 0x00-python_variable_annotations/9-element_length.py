#!/usr/bin/env python3

"""
9-element_length.py

This module provides a function to return a list of tuples
with the length of elements in the given iterable.
"""

from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples, where each tuple contains an element from
    the input iterable and its corresponding length.

    Parameters:
    lst (Iterable[Sequence]): The iterable containing sequences whose lengths
    are to be calculated.

    Returns:
    List[Tuple[Sequence, int]]: A list of tuples
    containing each element and its length.
    """
    return [(i, len(i)) for i in lst]

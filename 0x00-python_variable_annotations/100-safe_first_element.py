#!/usr/bin/env python3

"""
100-safe_first_element.py

This module provides a function to safely get the first element of a list.
"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of the list if it exists, otherwise returns None.

    Parameters:
    lst (Sequence[Any]): The list from which to retrieve the first element.

    Returns:
    Union[Any, None]: The first element of the list if it exists,
    otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None

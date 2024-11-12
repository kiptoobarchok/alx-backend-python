#!/usr/bin/env python3

"""
101-safely_get_value.py

This module provides a function to safely get a value from a dictionary.
"""

from typing import Any, Mapping, TypeVar, Union

T = TypeVar('T')


def safely_get_value(
    dct: Mapping,
    key: Any,
    default: Union[T, None] = None
) -> Union[Any, T]:
    """
    Safely gets a value from the dictionary using the given key.
    If the key is not present, returns the default value.

    Parameters:
    dct (Mapping): The dictionary from which to retrieve the value.
    key (Any): The key to look for in the dictionary.
    default (Union[T, None]): The default value to return
    if the key is not found.

    Returns:
    Union[Any, T]: The value associated with the key if it exists,
    otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default

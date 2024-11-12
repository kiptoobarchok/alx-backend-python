#!/usr/bin/env python3

"""
8-make_multiplier.py

This module provides a function that returns a multiplier function.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by a given multiplier.

    Parameters:
    multiplier (float): The multiplier to use in the returned function.

    Returns:
    Callable[[float], float]: A function that takes a float
    and returns it multiplied by the multiplier.
    """
    def multiplier_function(value: float) -> float:
        """
        Multiplies a float by the stored multiplier.

        Parameters:
        value (float): The float to be multiplied.

        Returns:
        float: The result of multiplying the input float by the multiplier.
        """
        return value * multiplier

    return multiplier_function

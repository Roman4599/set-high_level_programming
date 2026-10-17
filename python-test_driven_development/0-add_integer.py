#!/usr/bin/python3
"""Contains the add_integer function.

This project is written test first: every function starts with the
doctests of its tests/*.txt file, until they all pass.
"""


def add_integer(a, b=98):
    """Return the sum of a and b, cast to int when they are floats.
    Anything else raises a TypeError.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)

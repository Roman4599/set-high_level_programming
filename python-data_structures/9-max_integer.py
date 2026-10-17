#!/usr/bin/python3
"""Module that finds the biggest integer of a list."""


def max_integer(my_list=[]):
    """Return the biggest integer of my_list, or None if empty."""
    if len(my_list) == 0:
        return None
    big = my_list[0]
    for i in my_list:
        if i > big:
            big = i
    return big

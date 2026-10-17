#!/usr/bin/python3
"""Module that replaces an element in a copy of a list."""


def new_in_list(my_list, idx, element):
    """Return a copy of my_list with element at index idx replaced."""
    copy = my_list[:]
    if idx >= 0 and idx < len(copy):
        copy[idx] = element
    return copy

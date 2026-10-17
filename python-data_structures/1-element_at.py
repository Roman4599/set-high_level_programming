#!/usr/bin/python3
"""Module for retrieving an element from a list."""


def element_at(my_list, idx):
    """Return the element at index idx of my_list, or None."""
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]

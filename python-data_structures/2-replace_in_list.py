#!/usr/bin/python3
"""Module that replaces an element of a list."""


def replace_in_list(my_list, idx, element):
    """Replace the element at index idx of my_list with element."""
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list

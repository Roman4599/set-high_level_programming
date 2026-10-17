#!/usr/bin/python3
"""Module that removes all characters c and C from a string."""


def no_c(my_string):
    """Return my_string without the characters c and C."""
    new_string = ""
    for ch in my_string:
        if ch != 'c' and ch != 'C':
            new_string += ch
    return new_string

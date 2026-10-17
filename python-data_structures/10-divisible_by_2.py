#!/usr/bin/python3
"""Module that finds all multiples of 2 in a list."""


def divisible_by_2(my_list=[]):
    """Return a list telling whether each element of my_list is even."""
    return [i % 2 == 0 for i in my_list]

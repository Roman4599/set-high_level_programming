#!/usr/bin/python3
"""Defines a lookup function."""


def lookup(obj):
    """Return the list of attributes and methods of an object.

    Args:
        obj: object to inspect.
    """
    return dir(obj)

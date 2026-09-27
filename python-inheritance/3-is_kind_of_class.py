#!/usr/bin/python3
"""Defines an is_kind_of_class function."""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of a_class or of a subclass.

    Args:
        obj: object to check.
        a_class: class to compare against.
    """
    return isinstance(obj, a_class)

#!/usr/bin/python3
"""Contains the class_to_json function."""


def class_to_json(obj):
    """Return the dictionary describing the attributes of obj."""
    return obj.__dict__

#!/usr/bin/python3
"""Defines a MyList class."""


class MyList(list):
    """A list subclass able to print itself sorted."""

    def print_sorted(self):
        """Print the list in ascending sort order."""
        print(sorted(self))

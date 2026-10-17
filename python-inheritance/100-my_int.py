#!/usr/bin/python3
"""Defines a class MyInt that inherits from int."""


class MyInt(int):
    """Invert the == and != operators."""

    def __eq__(self, value):
        """Return True when the values differ."""
        return self.real != value

    def __ne__(self, value):
        """Return True when the values are equal."""
        return self.real == value

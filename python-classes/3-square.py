#!/usr/bin/python3
"""Defines a Square class with area calculation."""


class Square:
    """Represents a square with an area method."""

    def __init__(self, size=0):
        """Initialize a square with a validated size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current square area."""
        return self.__size ** 2

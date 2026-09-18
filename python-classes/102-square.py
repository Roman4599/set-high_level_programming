#!/usr/bin/python3
"""Defines a Square class with comparison operators."""


class Square:
    """Represents a square comparable by its area."""

    def __init__(self, size=0):
        """Initialize a square with a validated size."""
        self.size = size

    @property
    def size(self):
        """Retrieve the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size with type and value validation."""
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area."""
        return self.__size ** 2

    def __eq__(self, other):
        """Return True if both squares have equal area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Return True if both squares have different area."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Return True if self area is smaller."""
        return self.area() < other.area()

    def __le__(self, other):
        """Return True if self area is smaller or equal."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Return True if self area is bigger."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Return True if self area is bigger or equal."""
        return self.area() >= other.area()

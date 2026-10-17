#!/usr/bin/python3
"""Defines a Rectangle class tracking its number of instances."""


class Rectangle:
    """Represents a rectangle and counts its instances."""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize a rectangle and count a new instance."""
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width with type and value validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height with type and value validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the rectangle area."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the rectangle perimeter."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return the rectangle drawn with # characters."""
        if self.__width == 0 or self.__height == 0:
            return ""
        return (("#" * self.__width + "\n") * self.__height)[:-1]

    def __repr__(self):
        """Return a representation to recreate the rectangle."""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Decrement the counter and print a farewell message."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

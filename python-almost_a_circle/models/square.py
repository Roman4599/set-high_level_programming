#!/usr/bin/python3
"""Square class that inherits from Rectangle."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.

        Args:
            size (int): the size of the square.
            x (int): the horizontal offset.
            y (int): the vertical offset.
            id (int): the identity of the new square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get/set the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """Return the string representation of the square."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Update the square attributes.

        Args:
            *args: id, size, x, y in that order.
            **kwargs: attribute names and their new values.
        """
        if args:
            attrs = ("id", "size", "x", "y")
            for index, value in enumerate(args):
                if index < len(attrs):
                    setattr(self, attrs[index], value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of the square."""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }

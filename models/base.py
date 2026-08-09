#!/usr/bin/python3
"""Base class for all models."""

class Base:
    """Manages id attribute to avoid duplicate code."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize Base instance.
        Args:
            id (int): If provided, assign to instance; else auto-increment.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
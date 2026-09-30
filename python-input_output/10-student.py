#!/usr/bin/python3
"""Defines a Student class whose description can be filtered."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a student with a first name, a last name and an age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return the dictionary describing the student, filtered by attrs."""
        if attrs is None:
            return self.__dict__
        description = {}
        for attr in attrs:
            if hasattr(self, attr):
                description[attr] = getattr(self, attr)
        return description

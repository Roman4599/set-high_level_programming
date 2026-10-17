#!/usr/bin/python3
"""Defines a Student class that can be reloaded from a dictionary."""


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

    def reload_from_json(self, json):
        """Replace the attributes of the student with the ones in json."""
        for key, value in json.items():
            setattr(self, key, value)

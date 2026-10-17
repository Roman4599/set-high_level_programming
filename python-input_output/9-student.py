#!/usr/bin/python3
"""Defines a Student class."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a student with a first name, a last name and an age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return the dictionary describing the student."""
        return self.__dict__

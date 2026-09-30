#!/usr/bin/python3
"""Contains the append_write function."""


def append_write(filename="", text=""):
    """Append text to a file and return the number of characters added."""
    with open(filename, "a", encoding="utf-8", newline="") as f:
        return f.write(text)

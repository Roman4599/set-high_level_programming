#!/usr/bin/python3
"""Contains the write_file function."""


def write_file(filename="", text=""):
    """Write text to a file and return the number of characters written."""
    with open(filename, "w", encoding="utf-8", newline="") as f:
        return f.write(text)

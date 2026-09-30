#!/usr/bin/python3
"""Contains the append_after function."""


def append_after(filename="", search_string="", new_string=""):
    """Insert new_string after every line containing search_string."""
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()
    result = []
    for line in lines:
        result.append(line)
        if search_string in line:
            result.append(new_string)
    with open(filename, "w", encoding="utf-8", newline="") as f:
        f.writelines(result)

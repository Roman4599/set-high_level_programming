#!/usr/bin/python3
"""Adds the command line arguments to a list stored in a JSON file."""

import sys

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

FILENAME = "add_item.json"


def get_items():
    """Return the list stored in FILENAME, empty when the file is missing."""
    try:
        return load_from_json_file(FILENAME)
    except FileNotFoundError:
        return []


def add_items(items, arguments):
    """Return items extended with the given arguments."""
    return items + list(arguments)


if __name__ == "__main__":
    save_to_json_file(add_items(get_items(), sys.argv[1:]), FILENAME)

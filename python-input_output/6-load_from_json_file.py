#!/usr/bin/python3
"""Contains the load_from_json_file function."""

import json


def load_from_json_file(filename):
    """Return the object described by the JSON file filename."""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

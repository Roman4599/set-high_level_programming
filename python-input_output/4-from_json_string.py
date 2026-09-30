#!/usr/bin/python3
"""Contains the from_json_string function."""

import json


def from_json_string(my_str):
    """Return the object represented by the JSON string my_str."""
    return json.loads(my_str)

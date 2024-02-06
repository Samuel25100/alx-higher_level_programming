#!/usr/bin/python3
"""Functions load from json."""
import json


def load_from_json_file(filename):
    """Functions load json file to object."""
    with open(filename) as f:
        return json.load(f)

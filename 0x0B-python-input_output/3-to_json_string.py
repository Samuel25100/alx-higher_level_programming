#!/usr/bin/python3
"""Return the JSON representation of an object (string)."""
import json


def to_json_string(my_obj):
    """Serialize object my_obj using JSON module."""
    return json.dumps(my_obj)

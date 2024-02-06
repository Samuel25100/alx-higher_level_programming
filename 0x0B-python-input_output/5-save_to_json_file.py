#!/usr/bin/python3
"""Write an Object to a text file, using a JSON representation."""
import json


def save_to_json_file(my_obj, filename):
    """Write the object to a text file using json representation."""
    with open(filename, 'w') as f:
        json.dump(my_obj, f)

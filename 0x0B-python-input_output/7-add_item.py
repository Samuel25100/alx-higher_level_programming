#!/usr/bin/python3
"""Module add_item 'add_item.json' and copy from argv to it."""
import sys
import os
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


def add_item(args, filename):
    """Add item create new file 'add_item.json', add content argv."""
    if (os.path.exists(filename)):
        f = load_from_json_file(filename)
    else:
        f = []
    f.extend(args)
    save_to_json_file(f, filename)


if __name__ == "__main__":
    args = sys.argv[1:]
    filename = "add_item.json"
    add_item(args, filename)

#!/usr/bin/python3
"""Insert 'new_string' after line which include 'search_string'."""


def append_after(filename="", search_string="", new_string=""):
    """Insert 'new_string' after line of 'search_string'."""
    tmp_text = ""
    with open(filename) as f:
        for line in f:
            tmp_text += line
            if search_string in line:
                tmp_text += new_string
    with open(filename, 'w') as edit:
        edit.write(tmp_text)

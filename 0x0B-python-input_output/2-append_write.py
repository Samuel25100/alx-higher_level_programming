#!/usr/bin/python3
"""Function append_write write on file if already exist will apend."""


def append_write(filename="", text=""):
    """Append a string at the end of a text file (UTF8)."""
    with open(filename, 'a', encoding="UTF8") as f:
        f.write(text)
        num = len(text)
    return num

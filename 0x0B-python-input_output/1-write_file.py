#!/usr/bin/python3
"""write a string to a text file (UTF8), returns the num of char"""


def write_file(filename="", text=""):
    with open(filename, 'w', encoding="UTF8") as f:
        num = f.write(text)
    return (num)

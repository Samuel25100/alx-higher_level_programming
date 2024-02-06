#!/usr/bin/python3
"""Module pascal_triangle."""


def pascal_triangle(n):
    """Return list of lists of int with Pascal’s triangle of n."""
    if n <= 0:
        return []
    tri = []
    for i in range(1, n + 1):
        val = 1
        row = []
        for j in range(1, i + 1):
            row.append(val)
            val = val * (i - j) // j
        tri.append(row)
    return tri

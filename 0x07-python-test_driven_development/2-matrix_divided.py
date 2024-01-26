#!/usr/bin/python3
"""Divide the argument matrix to div return new matrix"""


def matrix_divided(matrix, div):
    if (not isinstance(matrix, list) and
            not all(isinstance(i, list) for i in matrix)):
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
    for i in matrix:
        for j in i:
            if not isinstance(j, (int, float)):
                raise TypeError(
                        "matrix must be a matrix (list of lists) \
of integers/floats")
    if (not all(len(matrix[0]) == len(i) for i in matrix)):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_mat = [[j/div for j in i]for i in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            new_mat[i][j] = round(new_mat[i][j], 2)
    return (new_mat)

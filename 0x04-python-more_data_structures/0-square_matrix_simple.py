#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_mat = []
    for i in matrix:
        new_mat.append([j**2 for j in i])
    return new_mat

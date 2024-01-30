#!/usr/bin/python3
"""Matrix multiplication"""


def matrix_mul(m_a, m_b):
    """Multiply matrix m_a and m_b and return new matrix."""
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    if any(not isinstance(i, list) for i in m_a):
        raise TypeError("m_a must be a list of lists")
    if any(not isinstance(i, list) for i in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    if any(not isinstance(j, (int, float)) for i in m_a for j in i):
        raise TypeError("m_a should contain only integers or floats")
    if any(not isinstance(j, (int, float)) for i in m_b for j in i):
        raise TypeError("m_b should contain only integers or floats")
    if any(len(m_a[0]) != len(i) for i in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if any(len(m_b[0]) != len(i) for i in m_b):
        raise TypeError("each row of m_b must be of the same size")

    rows_ma = len(m_a)
    cols_ma = len(m_a[0])
    cols_mb = len(m_b[0])
    if cols_ma != cols_mb:
        raise ValueError("m_a and m_b can't be multiplied")
    new_mat = [[0 for _ in range(cols_mb)] for _ in range(rows_ma)]
    for i in range(rows_ma):
        for j in range(cols_mb):
            for k in range(len(m_b)):
                new_mat[i][j] += m_a[i][k] * m_b[k][j]
    return (new_mat)

#!/usr/bin/env python3
"""
minor of a matrix
"""


def determinant(matrix):
    """
    Computes Determinant of a matrix
    Args:
        - matrix : the matrix on which we compute the determinant
    Returns:
        An Integer containing the determinant of the matrix
    """

    # there is no matrix
    if not matrix:
        raise TypeError('matrix must be a list of lists')

    # the shell is not a list
    if not isinstance(matrix, list):
        raise TypeError('matrix must be a list of lists')

    # each row has to be a list
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError('matrix must be a list of lists')

    # matrix with one row but that row is empty
    if len(matrix) == 1 and len(matrix[0]) == 0:
        return 1

    # list with one row and 1 element
    if len(matrix) == 1 and len(matrix[0]) == 1:
        return matrix[0][0]

    # matrix wih size m x n
    for row in matrix:
        if len(matrix) != len(row):
            raise ValueError('matrix must be a square matrix')

    # lentgh of the matrix
    n = len(matrix)

    # case if n = 2
    if (n == 2):
        return (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0])

    # recursivity for more than 2
    res = 0
    for i in range(n):
        if i % 2 == 0:
            res += matrix[0][i] * determinant([row[:i] + row[i + 1:]
                                           for row in matrix[1:]])
        else:
            res -= matrix[0][i] * determinant([row[:i] + row[i + 1:]
                                           for row in matrix[1:]])
    return res


def minor(matrix):
    """
    Computes minor of a matrix
    Args:
        - matrix : the matrix on which we compute the determinant
    Returns:
        A matrix containing the minors of the matrix
    """

    # there is no matrix
    if not matrix:
        raise TypeError('matrix must be a list of lists')

    # the shell is not a list
    if not isinstance(matrix, list):
        raise TypeError('matrix must be a list of lists')

    # each row has to be a list
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError('matrix must be a list of lists')

    # matrix wih size m x n
    for row in matrix:
        if len(matrix) != len(row):
            raise ValueError('matrix must be a non-empty square matrix')

    # empty matrix
    if (matrix == [] or matrix[0] == []):
        raise ValueError('matrix must be a non-empty square matrix')

    # lentgh of the matrix
    n = len(matrix)

    # case if n = 1
    if (n == 1):
        return [[1]]

    # case if n = 2
    if (n == 2):
        return [[matrix[1][1], matrix[1][0]], [matrix[0][1], matrix[0][0]]]

    # Solution for more than 2
    res = []
    for i in range(n):
        res.append([])
        for j in range(n):
            tmp = determinant([row[:j] + row[j + 1:] for row in (matrix[:i] + matrix[i + 1:])])
            res[i].append(tmp)
    return res
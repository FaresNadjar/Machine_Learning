#!/usr/bin.env python3
"""Definitiveness of Matrix"""

import numpy as np


def definiteness(matrix):
    """
    Function that calculates the definitness of a matrix
    Args:
       - matrix:    numpy.ndarray of shape (n, n) whose definiteness should
                    be calculated
        If matrix is not a numpy.ndarray, raise a TypeError with the message:
        matrix must be a numpy.ndarray
        If matrix is not a valid matrix, return None
    Return:
        - string Positive definite, Positive semi-definite, Negative
        semi-definite, Negative definite, or Indefinite if the matrix is
        positive definite, positive semi-definite, negative semi-definite,
        negative definite of indefinite, respectively
    Note: If matrix does not fit any of the above categories, return None
    """

    m = matrix

    # validate it is a numpy array
    if not isinstance(m, np.ndarray):
        raise TypeError("matrix must be a numpy.ndarray")

    # Is it a valid matrix ?
    if (matrix.size == 0) or (matrix.shape != (len(matrix), len(matrix))):
        return None

    # Is matrix symetrical ?
    if not (matrix.transpose() == matrix).all():
        return None

    # https://bit.ly/3fEKcim.
    eigenvalues = np.linalg.eigvals(m)

    if np.all(eigenvalues < 0):
        return "Negative definite"

    elif np.all(eigenvalues > 0):
        return "Positive definite"

    elif np.all(eigenvalues <= 0):
        return "Negative semi-definite"

    elif np.all(eigenvalues >= 0):
        return "Positive semi-definite"

    else:
        return "Indefinite"

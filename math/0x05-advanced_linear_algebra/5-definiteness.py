#!/usr/bin.env python3
"""Definitiveness of Matrix"""

import numpy as np


def definiteness(matrix):
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

    # Compute EigenValues
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

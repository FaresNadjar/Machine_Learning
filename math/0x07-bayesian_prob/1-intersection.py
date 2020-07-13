#!/usr/bin/env python3
"""
Module used to
"""

import numpy as np


def n_choose_x(n, x):
    n_fact = np.math.factorial(n)
    x_fact = np.math.factorial(x)
    nx_fact = np.math.factorial(n - x)
    return n_fact / (x_fact * nx_fact)


def likelihood(x, n, P):
    if not isinstance(n, (int, float)) or n <= 0:
        raise ValueError("n must be a positive integer")

    if not isinstance(x, (int, float)) or x < 0:
        message = "x must be an integer that is greater than or equal to 0"
        raise ValueError(message)

    if x > n:
        raise ValueError("x cannot be greater than n")

    if not isinstance(P, np.ndarray) or len(P.shape) != 1 or P.shape[0] < 1:
        raise TypeError("P must be a 1D numpy.ndarray")

    if np.any(P > 1) or np.any(P < 0):
        raise ValueError("All values in P must be in the range [0, 1]")

    binomial_coef = n_choose_x(n, x)
    success_rate = pow(P, x)
    failure_rate = pow(1 - P, n - x)

    likelihood = binomial_coef * success_rate * failure_rate

    return likelihood


def intersection(x, n, P, Pr):
    if not isinstance(Pr, np.ndarray):
        raise TypeError("Pr must be a numpy.ndarray with the same shape as P")

    if not isinstance(P, np.ndarray) or len(P.shape) != 1 or P.shape[0] < 1:
        raise TypeError("P must be a 1D numpy.ndarray")

    if (Pr.shape != P.shape):
        raise TypeError("Pr must be a numpy.ndarray with the same shape as P")

    if np.any(Pr > 1) or np.any(Pr < 0):
        raise ValueError("All values in Pr must be in the range [0, 1]")

    if not (np.isclose(np.sum(Pr), 1)):
        raise ValueError("Pr must sum to 1")

    # If events are independent , P(A ∩ B) = P(A) * P(B)
    # If not, P(A ∩ B) = P(B∣A) * P(A) / P(B)

    intersection = Pr * likelihood(x, n, P)
    return intersection

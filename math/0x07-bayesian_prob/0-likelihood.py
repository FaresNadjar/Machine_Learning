#!/usr/bin/env python3
"""
likelihood function
"""

import numpy as np

def likelihood(x, n, P):
    """
    likelihood function
    Args:
    - x: number of patients that develop severe side effects
    - n: total number of patients
    - P: 1D array containint the various prob of developping
     severe side effects
    Returns: 1D array contining the likelihood of obtaining
    the data, x and n, for each prob P, respectively.
    """

    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")

    if not isinstance(x, int) or x < 0:
        message = "x must be an integer that is greater than or equal to 0"
        raise ValueError(message)

    if x > n:
        raise ValueError("x cannot be greater than n")

    if not isinstance(P, np.ndarray) or len(P.shape) != 1 or P.shape[0] < 1:
        raise TypeError("P must be a 1D numpy.ndarray")

    if np.any(P > 1) or np.any(P < 0):
        raise ValueError("All values in P must be in the range [0, 1]")

    res = []

    for i in range(len(P)):
        tmp = np.math.factorial(n) / np.math.factorial(x)
        tmp = tmp / np.math.factorial(n - x) * P[i]**x
        tmp = tmp * (1 - P[i])**(n - x)
        res.append(tmp)
    return res

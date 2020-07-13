#!/usr/bin/env python3
""" Mean & Covariance """

import numpy as np


def mean_cov(X):
    if(isinstance(X, type(None))):
        raise TypeError('X must be a 2D numpy.ndarray')

    if (not isinstance(X, np.ndarray)) or (len(X.shape) != 2):
        raise TypeError('X must be a 2D numpy.ndarray')

    if X.shape[0] < 2:
        raise ValueError("X must contain multiple data points")

    mean = X.mean(axis=0)
    mean = np.reshape(mean, (-1, X.shape[1]))

    n = X.shape[0] - 1
    x = X - mean
    cov = np.dot(x.T, x) / n

    return mean, cov

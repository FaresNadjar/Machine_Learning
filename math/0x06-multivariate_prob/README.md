# Multivariate Probability
## Mean and Covariance
```python
#!/usr/bin/env python3
""" Mean & Covariance """

import numpy as np


def mean_cov(X):
    """
    Function that calculates the mean and covariance of a data set:
    Args:
        - X:        numpy.ndarray   Array of shape (n,d) containing
                    the data set:
            - n     int             number of data points
            - d     int             number of dimensions in each data point
        If X is not a 2D numpy.ndarray, raise a TypeError with the message:
        X must be a 2D numpy.ndarray
        If n is less than 2, raise a ValueError with the message
        X must contain multiple data points
    Returns:
        - mean, cov:
            - mean: numpy.ndarray   Array of shape (1, d) containing the
                                    mean of the data set
            - cov:  numpy.ndarray   Array of shape (d, d) containing the
                                    covariance matrix of the data set
    """
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
```

## Correlation
```python

#!/usr/bin/env python3
""" module """

import numpy as np


def correlation(C):
    """
    Function that calculates a correlation matrix:
    Args:
        - C:        numpy.ndarray   Array of shape (d, d) containing
                    a covariance matrix:
        If C is not a 2D numpy.ndarray, raise a TypeError with the message:
        C must be a numpy.ndarray
        If C does not have shape (d, d), raise a ValueError with the message
        C must be a 2D square matrix
        If n is less than 2, raise a ValueError with the message
        X must contain multiple data points
    Returns:
        - correlation   numpy ndarray   Matrix of shape (d, d) with its corr
    """
    if (isinstance(C, type(None))):
        raise TypeError('C must be a numpy.ndarray')

    if (not isinstance(C, np.ndarray)):
        raise TypeError('C must be a numpy.ndarray')

    if (len(C.shape) != 2):
        raise ValueError("C must be a 2D square matrix")

    if (C.shape[0] != C.shape[1]):
        raise ValueError("C must be a 2D square matrix")

    v = np.sqrt(np.diag(C))
    outer_v = np.outer(v, v)
    correlation = C / outer_v

    return correlation
```

## MultiNormal
```python
#!/usr/bin/env python3

"""
Class for the Multinirmal probabilities
"""

import numpy as np


class MultiNormal:
    """ Represents a Multivariate Normal distribution"""

    def __init__(self, data):
        """
        class constructor
        Args:
            - data:     numpy.ndarray       Array of shape (d, n) containing
                                            the dataset:
                - n     int             number of data points
                - d     int             number of dimensions in each data point
            If data is not a 2D numpy.ndarray, raise a TypeError with the msg:
            data must be a 2D numpy.ndarray
            If n is less than 2, raise a ValueError with the message
            data must contain multiple data points
            Set the public instance variables:
            mean - a numpy.ndarray of shape (d, 1) containing the mean of data
            cov -  a numpy.ndarray of shape (d, d) containing the covariance
            matrix data
        """

        if(isinstance(data, type(None))):
            raise TypeError('data must be a 2D numpy.ndarray')

        if (not isinstance(data, np.ndarray)) or (len(data.shape)) != 2:
            raise TypeError("data must be a 2D numpy.ndarray")

        if (data.shape[1] < 2):
            raise ValueError("data must contain multiple data points")

        data = data.T
        mean = data.mean(axis=0)
        mean = np.reshape(mean, (-1, data.shape[1]))

        n = data.shape[0] - 1
        x = data - mean
        cov = np.dot(x.T, x) / n

        self.mean = mean.T
        self.cov = cov

    def pdf(self, x):
        """
        Method that calculates the PDF at a data point:
        Args:
            - x:    np.ndarray  Array of shape (d, 1) with the data point
                                to calculate PDF
                    d           Int. number of dimensions of the Multinomial
                                instance
            If x is not a numpy.ndarray, raise a TypeError with the message
            x must by a numpy.ndarray
            If x is not of shape (d, 1), raise a ValueError with the message
            x mush have the shape ({d}, 1)
        Returns: The value of the PDF
        """

        d = self.cov.shape[0]

        if(isinstance(x, type(None))):
            raise TypeError('x must be a numpy.ndarray')

        if not isinstance(x, np.ndarray):
            raise TypeError("x must be a numpy.ndarray")

        if (x.shape[0] != d):
            raise ValueError("x must have the shape ({}, 1)".format(d))

        if (len(x.shape) != 2) or (x.shape[1] != 1):
            raise ValueError("x must have the shape ({}, 1)".format(d))

        mean = self.mean
        cov = self.cov

        x_m = x - mean
        pdf = (1. / (np.sqrt((2 * np.pi)**d * np.linalg.det(cov)))
               * np.exp(-(np.linalg.solve(cov, x_m).T.dot(x_m)) / 2))

        return pdf[0][0]
```

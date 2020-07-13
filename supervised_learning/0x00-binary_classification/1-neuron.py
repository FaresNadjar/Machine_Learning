#!/usr/bin/env python3
"""
Class Neuron
"""

import numpy as np


class Neuron:
    """ Class """

    def __init__(self, nx):
        """
        Initialize the Neuron class
        Arguments
        ---------
        - nx   : number of input features to the neuron
        Return
        ------
        Private attributes:
        - W    : The weights vector for the neuron.
                 It is initialized with a random normal distribution.
        - b    : The bias for the neuron. Upon instantiation.
                 It is initialized to 0.
        - A    : The activated output of the neuron (prediction).
                 It is initialized to 0.
        """

        if not(isinstance(nx, int)):
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be positive integer")

        self.__W = np.random.randn(1, nx)
        self.__b = 0
        self.__A = 0

    def get_W(self):
        return self.__W

    def get_b(self):
        return self.__b

    def get_A(self):
        return self.__A

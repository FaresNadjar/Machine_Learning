#!/usr/bin/env python3
"""
Class Neural Network
"""

import numpy as np


class NeuralNetwork:
    def __init__(self, nx, nodes):
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")

        if nx < 1:
            raise ValueError("nx must be a positive integer")

        if not isinstance(nodes, int):
            raise TypeError("nodes must be an integer")

        if nodes < 1:
            raise ValueError("nodes must be a positive integer")

        self.__W1 = np.random.randn(nodes, nx)
        self.__b1 = np.zeros((nodes, 1))
        self.__A1 = 0
        self.__W2 = np.random.randn(1, nodes)
        self.__b2 = 0
        self.__A2 = 0

    @property
    def W1(self):
        return self.__W1

    @property
    def b1(self):
        return self.__b1

    @property
    def A1(self):
        return self.__A1

    @property
    def W2(self):
        return self.__W2

    @property
    def b2(self):
        return self.__b2

    @property
    def A2(self):
        return self.__A2

    def forward_prop(self, X):
        # Aggregation Function for the first node
        sum1 = np.matmul(self.W1, X) + self.b1

        # Applying the activation function (sigmoid here) for first node
        forward1 = 1 / (1 + np.exp(-sum1))

        # Entering the output on A1
        self.__A1 = forward1

        # Aggregation Function for the first node
        sum2 = np.matmul(self.W2, self.__A1) + self.b2

        # Applying the activation function (sigmoid here) for first node
        forward2 = 1 / (1 + np.exp(-sum2))

        # Entering the output on A1
        self.__A2 = forward2


        return self.__A1, self.__A2

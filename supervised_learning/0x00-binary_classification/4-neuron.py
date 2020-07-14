#!/usr/bin/env python3
"""
Class Neuron
"""

import numpy as np


class Neuron:
    def __init__(self, nx):
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")

        if nx < 1:
            raise ValueError("nx must be a positive integer")

        self.__W = np.random.randn(1, nx)
        self.__b = 0
        self.__A = 0

    @property
    def W(self):
        return self.__W

    @property
    def A(self):
        return self.__A

    @property
    def b(self):
        return self.__b

    def forward_prop(self, X):
        # Aggregation Function
        sum = np.matmul(self.W, X)

        # Adding the bias
        sum = sum + self.b

        # Applying the activation function (sigmoid here)
        forward = 1 / (1 + np.exp(-sum))

        # Entering the output on A
        self.__A = forward
        return self.__A

    def cost(self, Y, A):
        r = -1 / Y.shape[1]
        A_hat = 1.0000001 - A
        Y_hat = 1 - Y
        cost = r * np.sum(np.multiply(Y, np.log(A)) + np.multiply(Y_hat, np.log(A_hat)))
        return cost

    def evaluate(self, X, Y):
        # Forward propagation for the predicted value
        predictions = self.forward_prop(X)

        # Calculate cost
        cost = self.cost(Y, self.__A)

        # Labels
        labels = np.where(predictions >= 0.5, 1, 0)

        return (labels, cost)

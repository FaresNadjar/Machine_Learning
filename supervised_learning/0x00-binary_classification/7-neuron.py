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

    def gradient_descent(self, X, Y, A, alpha=0.05):
        # Derivative respect to weight
        dw = np.matmul(X, (A - Y).T) / len(X[0])

        # Derivative respect to bias
        db = np.sum(A - Y) / len(X[0])

        # Update w: = α * dw, where ": = means actualization"
        self.__W = self.__W - (alpha * dw).T

        # Update b: = α * db, where ": = means actualization"
        self.__b = self.__b - (alpha * db).T

    def train(self, X, Y, iterations=5000, alpha=0.05, verbose=True, graph=True, step=100):
        if not isinstance(iterations, int):
            raise TypeError("iterations must be an integer")

        if (iterations <= 0):
            raise ValueError("iterations must be a positive integer")

        if not isinstance(alpha, float):
            raise TypeError("alpha must be a float")

        if (alpha <= 0):
            raise ValueError("alpha must be positive")

        if (verbose is True) or (graph is True):
            if not isinstance(step, int):
                raise TypeError("step must be an integer")
            if (step < 0) or (step > iterations):
                raise ValueError("step must be positive and <= iterations")

        cost_list = []
        for i in range(iterations + 1):
            self.__A = self.forward_prop(X)
            self.gradient_descent(X, Y, self.__A, alpha)
            cost = self.cost(Y, self.__A)
            if verbose is True:
                if (i % step == 0 or step == iterations):
                    print("Cost after {} iterations: {}".format(i, cost))
                    if i < iterations:
                        cost_list.append(cost)
        if graph is True:
            x_list = np.arange(0, iterations, step)
            y_list = cost_list
            plt.plot(x_list, y_list, linewidth=4)

            plt.title('Training Cost')
            plt.xlabel('iterations')
            plt.ylabel('cost')
            plt.show()
        return self.evaluate(X, Y)

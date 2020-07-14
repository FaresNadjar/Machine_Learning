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
        cost = self.cost(Y, self.__A2)

        # Labels
        labels = np.where(self.__A2 >= 0.5, 1, 0)

        return (labels, cost)

    def gradient_descent(self, X, Y, A1, A2, alpha=0.05):
        # Derivative respect to weight
        dw2 = np.dot((A2 - Y), A1.T) / len(X[0])
        tmp = np.dot(self.__W2.T, (A2 - Y)) * A1 * (1 - A1)
        dw1 = np.dot(tmp, X.T) / len(X[0])

        # Derivative respect to bias
        db2 = (A2 - Y).mean(axis=1, keepdims=True)
        db1 = tmp.mean(axis=1, keepdims=True)

        # Update w2 & b2
        self.__W2 = self.__W2 - (alpha * dw2)
        self.__b2 = self.__b2 - (alpha * db2)

        # Update w1 & b1
        self.__W1 = self.__W1 - (alpha * dw1)
        self.__b1 = self.__b1 - (alpha * db1)

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
        for _ in range(iterations):
            self.forward_prop(X)
            self.gradient_descent(X, Y, self.__A1, self.__A2, alpha)

        return(self.evaluate(X, Y))

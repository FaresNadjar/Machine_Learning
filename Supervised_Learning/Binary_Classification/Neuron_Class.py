#!/usr/bin/env python3
"""
Class Neuron
"""

import matplotlib.pyplot as plt
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
        Public attributes:
        - W    : The weights vector for the neuron.
                 It is initialized with a random normal distribution.
        - b    : The bias for the neuron. Upon instantiation.
                 It is initialized to 0.
        - A    : The activated output of the neuron (prediction).
                 It is initialized to 0.
        """
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")

        if nx < 1:
            raise ValueError("nx must be a positive integer")

        self.__W = np.random.randn(1, nx)
        #  Draw random weights from a normal dist.
        self.__b = 0
        self.__A = 0

    @property
    def W(self):
        """
        getter method
        Args:
            - self
        Return:
        - __W: The value of the attribute __W.
        """
        return self.__W

    @property
    def A(self):
        """
        getter method
        Args:
            - self
        Return:
        - __A: The value of the attribute __A.
        """
        return self.__A

    @property
    def b(self):
        """
        getter method
        Args:
            - self
        Return:
        - __b: The value of the attribute __b.
        """
        return self.__b

    def forward_prop(self, X):
        """
        Calculates the forward propagation of the neuron. It also updates the
        private attribute __A by using a sigmoid activation function

        Arguments
        ---------

        - X     : numpy.ndarray
                  Array with shape (nx, m) that contains the input data
             nx : int
                  number of input features to the neuron
             m  : int
                  number of examples
        Return
        ------
        - __A   : float
                  Value of the attribute __A.
        """
        # z = W.X + b
        z = np.matmul(self.W, X) + self.b
        # We used the sigmoid function, could use another one
        forward_prop = 1 / (1 + np.exp(-1 * z))
        self.__A = forward_prop
        return self.__A

    def cost(self, Y, A):
        """
        Calculates the cost of the model using logistic regression
        Arguments
        ---------
        - Y   : numpy.ndarray
                Array with shape (1, m) with the correct labels for the inputs
        - A   : numpy.ndarray
                Array with shape (1, m) containing the activated output of the
                neuron for each example
        Return:
        - cost: float
                the cost of the model
        """

        # Answer from: https://bit.ly/37x9YzM  - Compute cost
        m = Y.shape[1]
        j = - (1 / m)

        Â = 1.0000001 - A #1.00000001 to avoid division by 0 if A = 1
        Ŷ = 1 - Y
        log_A = np.log(A)
        log_Â = np.log(Â)
        cost = j * np.sum(np.multiply(Y, log_A) + np.multiply(Ŷ, log_Â))
        return cost

    def evaluate(self, X, Y):
        """
        Evaluates the neuron’s predictions

        Arguments

        - X          : numpy.ndarray
                       Array with shape (nx, m) that contains the input data
               nx    : int
                       number of input features to the neuron
               m     : int
                       number of examples
        - Y          : numpy.ndarray
                       Array with shape (1, m) that contains the correct
                       labels for the input data

        Returns
        neuron’s prediction (labels) and the cost of the network, respectively
        - prediction : numpy.ndarray
                       Array with shape (1, m) containing the predicted labels
                       for each example
                       - The label values should be 1 if the output of the
                         network is >= 0.5 and 0 otherwise
        - costs      : float
                       the cost of the model
        """

        # Generate the value of each activation
        predictions = self.forward_prop(X)

        # Calculate cost
        cost = self.cost(Y, self.__A)
        labels = np.where(predictions < 0.5, 0, 1)

        return (labels, cost)

    def gradient_descent(self, X, Y, A, alpha=0.05):
        """
        Calculates one pass of gradient descent on the neuron and updates the
        private attributes __W and __b

        Arguments
        - X            : numpy.ndarray
                         Array with shape (nx, m) & contains the input data
        - Y            : numpy.ndarray
                         Array with shape (1, m) that contains the correct
                         labels for the input data
        - A            : numpy.ndarray
                         Array with shape (1, m) containing the activated
                         output of the neuron for each example
        - alpha        : learning rate.

        Return
        The updaed valus of __W and __b
        """

        α = alpha
        m = 1 / len(X[0])

        # z = w1X1 + w2X2 + b
        # Derivative z: https://www.youtube.com/watch?v=z_xiwjEdAC4
        dz = A - Y

        # Derivative respect to weight
        dw = np.matmul(X, (dz).T) * m

        # Derivative respect to bias
        db = np.sum(dz) * m

        # Update w: = α * dw, where ": = means actualization"
        self.__W = self.__W - (α * dw).T

        # Update b: = α * db, where ": = means actualization"
        self.__b = self.__b - (α * db).T

    def train(self, X, Y, iterations=2000, alpha=0.05, verbose=True,
              graph=True, step=100):
        """
        Trains the neuron and updates __W, __b, and __A
        Arguments
        - X         : numpy.ndarray
                      Array with shape (nx, m) & contains the input data
        - Y         : numpy.ndarray
                      Array with shape (1, m) that contains the correct labels
                      for the input data
        - iterations: int
                      number of iterations to train over.
                    - if iterations is not an integer, raise a TypeError with
                      the exception iterations must be an integer
                    - if iterations is not positive, raise a ValueError with
                      the exception iterations must be a positive integer
        - alpha     : float
                      learning rate.
                    - if alpha is not a float, raise a TypeError with the
                      exception alpha must be a float
                    - if alpha is not positive, raise a ValueError with the
                      exception alpha must be positive
        - verbose   : bool
                      Defines whether or not to print information about the
                      training. If True, print Cost after {iteration}
                      iterations: {cost} every step iterations:
        - graph     : boolean
                      defines whether or not to graph information about the
                      training once the training has completed. If True:
                      Plot the training data every step iterations as a blue
                      line
                        Label the x-axis as iteration
                        Label the y-axis as cost
                        Title the plot Training Cost
                        Include data from the 0th and last iteration
        Only if either verbose or graph are True:
                        - if step is not an integer, raise a TypeError with
                          the exception step must be an integer
                        - if step is not positive or is greater than
                          iterations, raise a ValueError with the exception
                          step must be positive and <= iterations

        Return:
        - Eval      : float
                      the evaluation of the training data after iterations of
                      training have occurred
        """

        α = alpha

        if not isinstance(iterations, int):
            raise TypeError("iterations must be an integer")

        if (iterations <= 0):
            raise ValueError("iterations must be a positive integer")

        if not isinstance(alpha, float):
            raise TypeError("alpha must be a float")

        if (α <= 0):
            raise ValueError("alpha must be positive")

        if (verbose is True) or (graph is True):
            if not isinstance(step, int):
                raise TypeError("step must be an integer")
            if (step < 0) or (step > iterations):
                raise ValueError("step must be positive and <= iterations")

        cost_list = []
        for i in range(iterations + 1):
            self.__A = self.forward_prop(X)
            self.gradient_descent(X, Y, self.__A, α)
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

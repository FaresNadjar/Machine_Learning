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
            raise TypeErro("nodes must be an integer")

        if nodes < 1:
            raise ValueError("nodes must be a positive integer")

        self.W1 = np.random.randn(1, nx)
        self.b1 = 0
        self.A1 = 0
        self.W2 = np.random.randn(1, nx)
        self.b2 = 0
        self.A2 = 0

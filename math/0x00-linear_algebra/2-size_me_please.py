#!/usr/bin/env python3
import numpy as np

def matrix_shape(matrix):
    shape = [len(matrix)]
    test = matrix[0]
    while (isinstance(test, list)):
        shape.append(len(test))
        test=test[0]
    return (shape)

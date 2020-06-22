#!/usr/bin/env python3
def matrix_shape(matrix):
    """Retrieve a Matrix's Shape
    Returns:
    list: Matrix's Shape
    """
    shape = [len(matrix)]
    test = matrix[0]
    while (isinstance(test, list)):
        shape.append(len(test))
        test = test[0]
    return (shape)

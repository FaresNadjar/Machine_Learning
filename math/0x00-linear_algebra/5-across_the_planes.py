#!/usr/bin/env python3
def matrix_shape(matrix):
    shape = [len(matrix)]
    test = matrix[0]
    while (isinstance(test, list)):
        shape.append(len(test))
        test = test[0]
    return (shape)

def add_matrices2D(mat1, mat2):
    if (!mat1 or !mat2 or matrix_shape(mat1) != matrix_shape(mat2)):
        return None
    mat = []
    for i in range(len(mat1)):
        mat.append([])
        for j in range(len(mat1[0])):
            mat[i].append(mat1[i][j] + mat2[i][j])
    return mat

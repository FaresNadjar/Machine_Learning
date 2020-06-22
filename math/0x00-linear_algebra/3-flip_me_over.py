#!/usr/bin/env python3
def matrix_transpose(matrix):
    mat = []
    for i in range(len(matrix[0])):
        mat.append([])
        for j in range(len(matrix)):
            mat[i].append(matrix[j][i])
    return mat

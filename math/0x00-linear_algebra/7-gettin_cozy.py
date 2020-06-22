#!/usr/bin/env python3
def cat_matrices2D(mat1, mat2, axis=0):
    mat = []
    for i in mat1 :
        mat.append(i.copy())
    for i in range(len(mat2)) :
        if (axis == 0):
            mat.append(mat2[i])
        else:
            mat[i].append(mat2[i])
    return mat

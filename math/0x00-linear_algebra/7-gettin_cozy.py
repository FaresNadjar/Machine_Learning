#!/usr/bin/env python3
def cat_matrices2D(mat1, mat2, axis=0):
    if (axis == 0 and (len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0])):
        return None
    mat = []
    for i in mat1 :
        mat.append(i.copy())
    for i in range(len(mat2)) :
        if (axis == 0):
            mat.append(mat2[i])
        else:
            for j in mat2[i]:
                mat[i].append(j)
    return mat

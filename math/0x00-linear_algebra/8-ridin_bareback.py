#!/usr/bin/env python3
def mat_mul(mat1, mat2):
    if (len(mat1[0]) != len(mat2)):
        return None
    mat=[]
    for i in range(len(mat1)):
        mat.append([])
	for j in range(len(mat2[0])):
            s = 0
            for k in range(len(mat1[0])):
                s = s + (mat1[i][k] * mat2[k][j])
            mat[i].append(s)
    return mat

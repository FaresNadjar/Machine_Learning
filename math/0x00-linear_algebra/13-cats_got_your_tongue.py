#!/usr/bin/env python3
import numpy as np
def np_cat(mat1, mat2, axis=0):
    new = np.array(np.copy(mat1))
    np.concatenate(new, np.copy(mat2), axis)
    return new

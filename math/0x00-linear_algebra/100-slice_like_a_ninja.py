#!/usr/bin/env python3
def np_slice(matrix, axes={}):
    new = matrix
    for i in axes.keys() :
        if i == 0 :
            if len(axes[i]) == 1 :
                new = new[:axes[i][0]]
            elif len(axes[i]) == 2 :
                new = new[axes[i][0]:axes[i][1]]
            else :
                new = new[::axes[i][2]]
        elif i == 1 :
            if len(axes[i]) == 1 :
                new = new[:,:axes[i][0]]
            elif len(axes[i]) == 2 :
                new = new[:,axes[i][0]:axes[i][1]]
            else :
                new = new[:,::axes[i][2]]
        elif i == 2 :
            if len(axes[i]) == 1 :
                new = new[:,:,:axes[i][0]]
            elif len(axes[i]) == 2 :
                new = new[:,:,axes[i][0]:axes[i][1]]
            else :
                new = new[:,:,::axes[i][2]]
    return new

#!/usr/bin/env python3
import numpy as np
def convolve_grayscale_same(images, kernel):
    l = []
    for im in images :
        im = np.pad(im, (1,1), "constant", constant_values=(0,0))
        res = np.zeros((im.shape[0] - kernel.shape[0] + 1, im.shape[1] - kernel.shape[1] + 1))
        for i in range(im.shape[0] - kernel.shape[0] + 1):
            for j in range(im.shape[1] - kernel.shape[1] + 1):
                res[i,j] = np.sum(im[i:i+kernel.shape[0],j:j+kernel.shape[1]] * kernel)
        l.append(res)
    return np.array(l)

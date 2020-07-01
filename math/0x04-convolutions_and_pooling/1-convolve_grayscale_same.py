#!/usr/bin/env python3
"""
Same
"""

import numpy as np


def convolve_grayscale_same(images, kernel):
    """Performs a same convolution on grayscale images.
    Args:
        images (np.ndarray): matrix of shape (m, h, w) containing multiple
                             grayscale images.
        kernel (np.ndarray): matrix of shape (kh, kw) containing the kernel
                             for the convolution.
    Returns:
        np.ndarray: The convolved images.
    """
    images = np.pad(images, ((0,0), (1,1), (1,1)), 'constant', constant_values=(0,0))
    m, h, w = images.shape
    kh, kw = kernel.shape

    ch = h - kh + 1
    cw = w - kw + 1
    
    res = np.zeros((m, ch, cw))
    
    for j in range(ch):
        for k in range(cw):
            images_slide = images[:, j:j + kh, k:k + kw]
            elem_mul = np.multiply(images_slide, kernel)
            res[:, j, k] = elem_mul.sum(axis=1).sum(axis=1)
    print(res.shape)
    return res

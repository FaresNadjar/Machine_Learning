#!/usr/bin/env python3
"""
Convolution using padding
"""

import numpy as np


def convolve_grayscale_padding(images, kernel, padding):
    # num images
    n_images = images.shape[0]

    # input_width and input_height
    i_h = images.shape[1]
    i_w = images.shape[2]

    # kernel_width and kernel_height
    k_h = kernel.shape[0]
    k_w = kernel.shape[1]

    # pad_h and pad_w ⊛
    p_h = padding[0]
    p_w = padding[1]

    # output_height and output_width
    o_h = i_h + 2 * p_h - k_h + 1
    o_w = i_w + 2 * p_w - k_w + 1

    # creating outputs of size: n_images, o_h x o_w
    outputs = np.zeros((n_images, o_h, o_w))

    # creating pad of zeros around the output images
    padded_imgs = np.pad(images,
                         ((0, 0), (p_h, p_h), (p_w, p_w)),
                         mode="constant",
                         constant_values=0)

    # vectorizing the n_images into an array
    imgs_arr = np.arange(0, n_images)

    # iterating over the output array and generating the convolution
    for x in range(o_h):
        for y in range(o_w):
            x1 = x + k_h
            y1 = y + k_w
            outputs[imgs_arr, x, y] = np.sum(np.multiply(
                padded_imgs[imgs_arr, x: x1, y: y1], kernel), axis=(1, 2))

    return outputs

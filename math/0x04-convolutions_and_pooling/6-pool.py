#!/usr/bin/env python3
"""
Module used to
"""

import numpy as np


def pool(images, kernel_shape, stride, mode='max'):
    # num images
    n_images = images.shape[0]

    # input_width and input_height
    i_h = images.shape[1]
    i_w = images.shape[2]

    # images channel
    i_c = images.shape[3]

    # kernel_width and kernel_height
    k_h = kernel_shape[0]
    k_w = kernel_shape[1]

    # stride_height and stride_width
    s_h = stride[0]
    s_w = stride[1]

    # output_height and output_width
    o_h = int((i_h - k_h) / s_h) + 1
    o_w = int((i_w - k_w) / s_w) + 1

    # creating outputs of size: [n_images,  o_h  ⊛  o_w  ⊛  k_c ⊛  i_c]
    outputs = np.zeros((n_images, o_h, o_w, i_c))

    # vectorizing the n_images into an array (creating a new dimension)
    imgs_arr = np.arange(0, n_images)

    # funtion selector
    funct = np.max
    if (mode == "avg"):
        funct = np.average

    # iterating over the output array and generating the pooling
    for x in range(o_h):
        for y in range(o_w):
            x0 = x * s_h
            y0 = y * s_w
            x1 = x0 + k_h
            y1 = y0 + k_w
            outputs[imgs_arr, x, y] = funct(images[imgs_arr, x0: x1, y0: y1],
                                            axis=(1, 2))

    return outputs

#!/usr/bin/env python3
"""
Convolution with channels
"""

import numpy as np


def convolve_channels(images, kernel, padding='same', stride=(1, 1)):
    # num images
    n_images = images.shape[0]

    # input_width and input_height
    i_h = images.shape[1]
    i_w = images.shape[2]

    # images channel
    i_c = images.shape[3]

    # kernel_width and kernel_height
    k_h = kernel.shape[0]
    k_w = kernel.shape[1]

    # stride_height and stride_width
    s_h = stride[0]
    s_w = stride[1]

    # pad_h and pad_w ⊛
    p_h = 0
    p_w = 0

    if (padding == "same"):
        p_h = int(((i_h - 1) * s_h + k_h - i_h) / 2) + 1
        p_w = int(((i_w - 1) * s_w + k_w - i_w) / 2) + 1

    elif (isinstance(padding, tuple)):
        p_h = padding[0]
        p_w = padding[1]

    # output_height and output_width
    o_h = int((i_h + 2 * p_h - k_h) / s_h) + 1
    o_w = int((i_w + 2 * p_w - k_w) / s_w) + 1

    # creating outputs of size: n_images, o_h x o_w
    outputs = np.zeros((n_images, o_h, o_w))

    # creating pad of zeros around the output images
    padded_imgs = np.pad(images,
                         ((0, 0),       # dim n_images
                          (p_h, p_h),   # dim height
                          (p_w, p_w),   # dim width
                          (0, 0)        # dim channels
                          ),
                         mode="constant",
                         constant_values=0)

    # vectorizing the n_images into an array (creating a new dimension)
    imgs_arr = np.arange(0, n_images)

    # vectorizing the n_images into an array (creating a new dimension)
    chan_arr = np.arange(0, i_c)

    # iterating over the output array and generating the convolution
    for x in range(o_h):
        for y in range(o_w):
            x0 = x * s_h
            y0 = y * s_w
            x1 = x0 + k_h
            y1 = y0 + k_w
            outputs[imgs_arr, x, y] = np.sum(np.multiply(
                padded_imgs[imgs_arr, x0: x1, y0: y1], kernel),
                axis=(1, 2, 3))

    return outputs

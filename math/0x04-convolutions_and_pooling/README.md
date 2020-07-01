# Convolution & Pooling
## Valid Convolution :
```python
#!/usr/bin/env python3
"""
Valid Convolution
"""

import numpy as np


def convolve_grayscale_valid(images, kernel):
    """
    Performs a valid convolution on grayscale images
    Args:
        - images is a numpy.ndarray with shape (m, h, w) containing
          multiple grayscale images
            - m is the number of images
            - h is the height in pixels of the images
            - w is the width in pixels of the images
        - kernel is a numpy.ndarray with shape (kh, kw) containing the kernel
          for the convolution
            - kh is the height of the kernel
            - kw is the width of the kernel
    Returns:
        A numpy.ndarray containing the convolved images
    """

    # num images
    n_images = images.shape[0]

    # input_width and input_height
    i_h = images.shape[1]
    i_w = images.shape[2]

    # kernel_width and kernel_height
    k_h = kernel.shape[0]
    k_w = kernel.shape[1]

    # output_height and output_width
    o_h = i_h - k_h + 1
    o_w = i_w - k_w + 1

    # pad ⊛
    pad = 1

    # creating outputs of size: n_images, o_h x o_w
    outputs = np.zeros((n_images, o_h, o_w))

    # vectorizing the n_images
    images_array = np.arange(0, n_images)

    # iterating over the output array and generating the convolution
    for x in range(o_h):
        for y in range(o_w):
            x1 = x + k_h
            y1 = y + k_w
            outputs[images_array, x, y] = np.sum(np.multiply(
                images[images_array, x: x1, y: y1], kernel), axis=(1, 2))

    return outputs
```
## Same Convolution :
```python
#!/usr/bin/env python3
"""
Same Convolution
"""

import numpy as np


def convolve_grayscale_same(images, kernel):
    """
    Performs a Same convolution on grayscale images
    Args:
        - images is a numpy.ndarray with shape (m, h, w) containing
          multiple grayscale images
            - m is the number of images
            - h is the height in pixels of the images
            - w is the width in pixels of the images
        - kernel is a numpy.ndarray with shape (kh, kw) containing the kernel
          for the convolution
            - kh is the height of the kernel
            - kw is the width of the kernel
    Returns:
        A numpy.ndarray containing the convolved images
    """

    # num images
    n_images = images.shape[0]

    # input_width and input_height
    i_h = images.shape[1]
    i_w = images.shape[2]

    # kernel_width and kernel_height

    k_h = kernel.shape[0]
    k_w = kernel.shape[1]

    # pad_h ⊛ = int (k_h - 1)/2
    # pad_w ⊛ = int (k_w - 1)/2
    p_h = int((k_h - 1) / 2)
    p_w = int((k_w - 1) / 2)

    if k_h % 2 == 0:
        p_h = int(k_h / 2)

    if k_w % 2 == 0:
        p_w = int(k_w / 2)

    # output_height and output_width
    # H = i_h + 2pad - k_h + 1, W = i_w + 2pad - k_w + 1
    o_h = i_h + 2 * p_h - k_h + 1
    o_w = i_w + 2 * p_w - k_w + 1

    if k_h % 2 == 0:
        o_h = i_h + 2 * p_h - k_h

    if k_w % 2 == 0:
        o_w = i_w + 2 * p_w - k_w

    # creating outputs of size: n_images, o_h x o_w
    outputs = np.zeros((n_images, o_h, o_w))

    # creating pad of zeros around the output images
    padded_imgs = np.pad(images,
                         pad_width=((0, 0), (p_h, p_h), (p_w, p_w)),
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
```

## Convolution with Padding
```python
#!/usr/bin/env python3
"""
Convolution using padding
"""

import numpy as np


def convolve_grayscale_padding(images, kernel, padding):
    """
    Performs a valid convolution on grayscale images
    Args:
        - images is a numpy.ndarray with shape (m, h, w) containing
          multiple grayscale images
            - m is the number of images
            - h is the height in pixels of the images
            - w is the width in pixels of the images
        - kernel is a numpy.ndarray with shape (kh, kw) containing the kernel
          for the convolution
            - kh is the height of the kernel
            - kw is the width of the kernel
        - padding is a tuple of (ph, pw)
            - ph is the padding for the height of the image
            - pw is the padding for the width of the image
        the image should be padded with 0’s
    Returns:
        A numpy.ndarray containing the convolved images
    """

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
```

## Strided Convolution
```python
#!/usr/bin/env python3
"""
Strided Convolution
"""

import numpy as np


def convolve_grayscale(images, kernel, padding='same', stride=(1, 1)):
    """
    Performs a valid convolution on grayscale images
    Args:
        - images is a numpy.ndarray with shape (m, h, w) containing
          multiple grayscale images
            - m is the number of images
            - h is the height in pixels of the images
            - w is the width in pixels of the images
        - kernel is a numpy.ndarray with shape (kh, kw) containing the kernel
          for the convolution
            - kh is the height of the kernel
            - kw is the width of the kernel
        - padding is either a tuple of (ph, pw), ‘same’, or ‘valid’
            - if ‘same’, performs a same convolution
            - if ‘valid’, performs a valid convolution
            - if a tuple:
                - ph is the padding for the height of the image
                - pw is the padding for the width of the image
            the image should be padded with 0’s
        - stride is a tuple of (sh, sw)
            - sh is the stride for the height of the image
            - sw is the stride for the width of the image
    Returns:
        A numpy.ndarray containing the convolved images
    """

    # num images
    n_images = images.shape[0]

    # input_width and input_height
    i_h = images.shape[1]
    i_w = images.shape[2]

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
    o_h = np.floor(((i_h + 2 * p_h - k_h) / s_h) + 1).astype(int)
    o_w = np.floor(((i_w + 2 * p_w - k_w) / s_w) + 1).astype(int)

    # creating outputs of size: n_images, o_h x o_w
    outputs = np.zeros((n_images, o_h, o_w))

    # creating pad of zeros around the images
    padded_imgs = np.pad(images,
                         ((0, 0), (p_h, p_h), (p_w, p_w)),
                         mode="constant",
                         constant_values=0)

    # vectorizing the n_images into an array
    imgs_arr = np.arange(0, n_images)

    # iterating over the output array and generating the convolution
    for x in range(o_h):
        for y in range(o_w):
            x0 = x * s_h
            y0 = y * s_w
            x1 = x0 + k_h
            y1 = y0 + k_w
            outputs[imgs_arr, x, y] = np.sum(np.multiply(
                padded_imgs[imgs_arr, x0: x1, y0: y1], kernel), axis=(1, 2))

    return outputs
```

## Convolution with Channels :
```python
#!/usr/bin/env python3
"""
Convolution with Channels
"""

import numpy as np


def convolve_channels(images, kernel, padding='same', stride=(1, 1)):
    """
    Performs a valid convolution on images with channels (colors)
    Args:
        - images is a numpy.ndarray with shape (m, h, w, c) containing
          multiple grayscale images
            - m is the number of images
            - h is the height in pixels of the images
            - w is the width in pixels of the images
            - c is the number of channels in the image
        - kernel is a numpy.ndarray with shape (kh, kw, c)
          containing the kernel for the convolution
            - kh is the height of the kernel
            - kw is the width of the kernel
            - c is the number of channels in the image
        - padding is either a tuple of (ph, pw), ‘same’, or ‘valid’
            - if ‘same’, performs a same convolution
            - if ‘valid’, performs a valid convolution
            - if a tuple:
                - ph is the padding for the height of the image
                - pw is the padding for the width of the image
            the image should be padded with 0’s
        - stride is a tuple of (sh, sw)
            - sh is the stride for the height of the image
            - sw is the stride for the width of the image
    Returns:
        A numpy.ndarray containing the convolved images
    """

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
```

## Multiple Kernels
```python
#!/usr/bin/env python3
"""
Module used to
"""

import numpy as np


def convolve(images, kernels, padding='same', stride=(1, 1)):
    """
    Performs a valid convolution on images with multiple channels (colors)
    Args:
        - images is a numpy.ndarray with shape (m, h, w, c) containing
          multiple grayscale images
            - m is the number of images
            - h is the height in pixels of the images
            - w is the width in pixels of the images
            - c is the number of channels in the image
        - kernels is a numpy.ndarray with shape (kh, kw, c)
          containing the kernel for the convolution
            - kh is the height of the kernel
            - kw is the width of the kernel
            - nc is the number of kernels
        - padding is either a tuple of (ph, pw), ‘same’, or ‘valid’
            - if ‘same’, performs a same convolution
            - if ‘valid’, performs a valid convolution
            - if a tuple:
                - ph is the padding for the height of the image
                - pw is the padding for the width of the image
            the image should be padded with 0’s
        - stride is a tuple of (sh, sw)
            - sh is the stride for the height of the image
            - sw is the stride for the width of the image
    Returns:
        A numpy.ndarray containing the convolved images
    """

    # num images
    n_images = images.shape[0]

    # input_width and input_height
    i_h = images.shape[1]
    i_w = images.shape[2]

    # images channel
    i_c = images.shape[3]

    # kernel_width and kernel_height
    k_h = kernels.shape[0]
    k_w = kernels.shape[1]

    # numer of channels of the kernel
    k_c = kernels.shape[3]

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

    # creating outputs of size: [n_images,  o_h  ⊛  o_w  ⊛  k_c ⊛  i_c]
    outputs = np.zeros((n_images, o_h, o_w, k_c))

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

    # iterating over the output array and generating the convolution
    for x in range(o_h):
        for y in range(o_w):
            for z in range(k_c):
                x0 = x * s_h
                y0 = y * s_w
                x1 = x0 + k_h
                y1 = y0 + k_w
                outputs[imgs_arr, x, y, z] = np.sum(np.multiply(
                    padded_imgs[imgs_arr, x0: x1, y0: y1],
                    kernels[:, :, :, z]), axis=(1, 2, 3))

    return outputs
```

## Pooling
```python
#!/usr/bin/env python3
"""
Module used to
"""

import numpy as np


def pool(images, kernel_shape, stride, mode='max'):
    """
    Performs a valid convolution on grayscale images
    Args:
        - images is a numpy.ndarray with shape (m, h, w, c) containing
          multiple grayscale images
            - m is the number of images
            - h is the height in pixels of the images
            - w is the width in pixels of the images
            - c is the number of channels in the image
        - kernel_shape is a numpy.ndarray with shape (kh, kw) containing
          the shape of the pooling
            - kh is the height of the kernel
            - kw is the width of the kernel
        - stride is a tuple of (sh, sw)
            - sh is the stride for the height of the image
            - sw is the stride for the width of the image
        - mode is a tuple of (sh, sw)
            - max indicates max pooling
            - avg indicates average pooling
    Returns:
        A numpy.ndarray containing the pooled images
    """

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
```

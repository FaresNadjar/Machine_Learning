#!/usr/bin/env python3
def convolve_grayscale_valid(images, kernel):
    l = []
    for im in images :
        res = np.zeros((im.shape[0] - kernel.shape[0] + 1, im.shape[1] - kernel.shape[1] + 1))
        for i in range(im.shape[0] - kernel.shape[0] + 1):
            for j in range(im.shape[1] - kernel.shape[1] + 1):
                res[i,j] = np.sum(im[i:i+kernel.shape[0],j:j+kernel.shape[1]] * kernel)
        l.append(res)
    return np.array(l)

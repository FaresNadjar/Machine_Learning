#!/usr/bin/env python3
def cat_arrays(arr1, arr2):
    arr = arr1.copy()
    for i in arr2:
        arr.append(i)
    return arr
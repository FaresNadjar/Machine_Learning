#!/usr/bin/env python3
def summation_i_squared(n):
    if n <= 0:
        return None
    s = 0
    for i in range(1, n + 1):
        s = s + (i * i)
    return s

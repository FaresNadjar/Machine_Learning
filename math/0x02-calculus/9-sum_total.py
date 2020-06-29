#!/usr/bin/env python3
def summation_i_squared(n) :
    if n <= 0 :
        return None
    return sum(i**2 for i in range(1, n + 1)

#!/usr/bin/env python3
def poly_derivative(poly):
    if not(poly):
        return None
    if (len(poly) == 0):
        return [0]
    l = []
    for i in range(1, len(poly)) :
        l.append(poly[i] * i)
    return l

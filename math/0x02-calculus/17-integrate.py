#!/usr/bin/env python3
def poly_integral(poly, C=0):
    if (not(poly) or not(isinstance(poly, list)) or not(isinstance(C, int))):
        return None
    new = [C]
    for i in range(len(poly)):
        new.append(poly[i] / i)
    return new

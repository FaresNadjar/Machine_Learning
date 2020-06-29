#!/usr/bin/env python3
def poly_integral(poly, C=0):
    if (not(poly) or not(isinstance(poly, list)) or not(isinstance(C, int))):
        return None
    new = [C]
    for i in range(len(poly)):
        if (poly[i] == 0):
            new.append(0)
        else:
            new.append(poly[i] / (i + 1))
    return new

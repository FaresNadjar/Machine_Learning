#!/usr/bin/env python3
def poly_integral(poly, C=0):
    if (not(poly) or not(isinstance(poly, list)) or not(isinstance(C, int))):
        return None
    new = [C]
    for i in range(1, len(poly)):
        if (poly[i] == 0):
            new.append(0)
        else:
            res = (poly[i] / (i + 1))
            if (res == int(res)):
                res = int(res)
            new.append(res)
    return new

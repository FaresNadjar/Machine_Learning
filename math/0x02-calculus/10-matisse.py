#!/usr/bin/env python3
def poly_derivative(poly):
    if (not(poly) or not(isinstance(poly, list))):
        return None
    if (len(poly) <= 1):
        return [0]
    new = []
    for i in range(1, len(poly)):
        new.append(poly[i] * i)
    return new

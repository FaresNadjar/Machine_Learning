#!/usr/bin/env python3
class poisson:
    def __init__(self, data=None, lambtha=1.):
        if data == None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            else:
                lambtha = self.lambtha
        else:
            if not(isinstance(data, list)):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            else:
                lambtha = sum(data) / len(data)

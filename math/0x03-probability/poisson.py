#!/usr/bin/env python3
class Poisson:
    def __init__(self, data=None, lambtha=1.):
        if data == None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            else:
                self.lambtha = lambtha
        else:
            if not(isinstance(data, list)):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            else:
                self.lambtha = sum(data) / len(data)
    def pmf(self, k):
        import math
        if not(isinstance(k, int)) :
            k = int(k)
        if k <= 0:
            return 0
        s = 1
        for i in range(1, k + 1) :
            s = s * i
        res = (self.lambtha**k) * math.exp(-self.lambtha) / s
        return res

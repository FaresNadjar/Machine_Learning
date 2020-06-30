#!/usr/bin/env python3
class Binomial:
    def __init__(self, data=None, n=1, p=0.5):
        if data is None:
            if n <= 0:
                raise ValueError("n must be a positive value")
            elif (p <= 0 or p >= 1):
                raise ValueError("p must be greater than 0 and less than 1")
            else:
                self.n = int(n)
            self.p = float(p)
        else:
            if not(isinstance(data, list)):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            else:
                E = sum(data) / len(data)
                EE = sum(i * i for i in data) / len(data)
                V = EE - E**2
                self.p = 1 - (V / E)
                self.n = round(V / self.p / (1 - self.p))
                self.p = E / self.n

    def pmf(self, k):
        if not(isinstance(k, int)):
            k = int(k)
        if k < 0:
            return 0
        if self.n == 0:
            nfact = 1
        else:
            nfact = 1
            for i in range(1, self.n + 1):
                nfact = nfact * i
        if k == 0:
            kfact = 1
        else:
            kfact = 1
            for i in range(1, k + 1):
                kfact = kfact * i
        if self.n - k == 0:
            nkfact = 1
        else:
            nkfact = 1
            for i in range(1, self.n - k + 1):
                nkfact = nkfact * i
        Cnk = nfact / kfact / nkfact
        res = Cnk * self.p**k
        res = res * (1 - self.p)**(self.n - k)
        return res

    def cdf(self, k):
        if not(isinstance(k, int)):
            k = int(k)
        if k < 0:
            return 0
        if k >= self.n:
            return 1
        return sum(self.pmf(i) for i in range(int(k) + 1))

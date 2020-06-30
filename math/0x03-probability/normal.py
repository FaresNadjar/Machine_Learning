#!/usr/bin/env python3
class Normal:
    def __init__(self, data=None, mean=0., stddev=1.):
        if data is None:
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
            else:
                self.stddev = float(stddev)
            self.mean = float(mean)
        else:
            if not(isinstance(data, list)):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            else:
                self.mean = sum(data) / len(data)
                EE = sum(i * i for i in data) / len(data) 
                self.stddev = (EE - self.mean**2)**(1 / 2)

    def z_score(self, x):
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        return (z * self.stddev) + self.mean

    def pdf(self, x):
        PI = 3.1415926536
        e = 2.7182818285
        z = self.z_score(x)
        t = (2 * PI)**(-1 / 2) * e**(-(z**2) / 2) / self.stddev
        return t

    def cdf(self, x):
        PI = 3.1415926536
        z = self.z_score(x)
        x = z / (2**(1 / 2))
        erf = 2 * (x - (x**3 / 3) + (x**5 / 10) - (x**7 / 42) + (x**9 / 216)) / (PI**(1 / 2))
        return (1 + erf) / 2

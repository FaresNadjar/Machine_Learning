# Binary Classification
## Neuron
```python
#!/usr/bin/env python3
"""
Class Neuron
"""

import numpy as np


class Neuron:
    def __init__(self, nx):
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")

        if nx < 1:
            raise ValueError("nx must be a positive integer")

        self.W = np.random.randn(1, nx)
        self.b = 0
        self.A = 0
```

## Privatise Neuron
```python
#!/usr/bin/env python3
"""
Class Neuron
"""

import numpy as np


class Neuron:
    def __init__(self, nx):
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")

        if nx < 1:
            raise ValueError("nx must be a positive integer")

        self.__W = np.random.randn(1, nx)
        #  Draw random samples from a normal dist.
        self.__b = 0
        self.__A = 0

    @property
    def W(self):
        return self.__W

    @property
    def A(self):
        return self.__A

    @property
    def b(self):
        return self.__b
```

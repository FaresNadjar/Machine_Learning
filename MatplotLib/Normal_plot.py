#!/usr/bin/env python3
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# How to plot (x,y)

# 0. y_data
y_data = np.arange(0, 11) ** 3

# 1. x data
x_data = range(0, 11)

# 2. Colors
line_color = "r"  # r for red
plt.figure(figsize=(10, 7)).set_facecolor("white")  # size & background color

# 3. limits for x_axis and y_axis
plt.xlim(0, 10)
plt.ylim(-50, 1050)

# 4. font
plt.rcParams.update({'font.size': 16})

# display
plt.plot(x_data, y_data, line_color, linewidth=3)
plt.grid(False)
plt.show()

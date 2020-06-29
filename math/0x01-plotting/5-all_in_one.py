#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

#Figure 1
y0 = np.arange(0, 11) ** 3
x0=range(11)

#Figure 2
mean = [69, 0]
cov = [[15, 8], [8, 15]]
np.random.seed(5)
x1, y1 = np.random.multivariate_normal(mean, cov, 2000).T
y1 += 180

#Figure 3
x2 = np.arange(0, 28651, 5730)
r2 = np.log(0.5)
t2 = 5730
y2 = np.exp((r2 / t2) * x2)

#Figure 4
x3 = np.arange(0, 21000, 1000)
r3 = np.log(0.5)
t31 = 5730
t32 = 1600
y31 = np.exp((r3 / t31) * x3)
y32 = np.exp((r3 / t32) * x3)

#Figure 5
np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

# Set up the axes with gridspec
fig = plt.figure(figsize=(10, 10))
grid = plt.GridSpec(3, 2, wspace=0.2, hspace=0.3)
plt.title("All in One", fontsize='large')
plt.axis('off')

Fig1 = fig.add_subplot(grid[0, 0])
Fig2 = fig.add_subplot(grid[0, 1])
Fig3 = fig.add_subplot(grid[1, 0])
Fig4 = fig.add_subplot(grid[1, 1])
Fig5 = fig.add_subplot(grid[2, :]);

Fig1.plot(x0,y0)
Fig2.scatter(x1, y1, c='magenta')
Fig2.set_ylabel("Weight (lbs)", fontsize='x-small')
Fig2.set_xlabel("Height (in)", fontsize='x-small')
Fig2.set_title("Men's Height vs Weight", fontsize='x-small')
Fig3.plot(x2, y2)
Fig3.set_yscale("log")
Fig3.set_xlabel("Time (years)", fontsize='x-small')
Fig3.set_ylabel("Fraction Remaining", fontsize='x-small')
Fig3.set_title("Exponential Decay of C-14", fontsize='x-small')
Fig4.plot(x3,y31, 'r--', label='C-14')
Fig4.plot(x3, y32, 'g', label="Ra-226")
Fig4.set_xlabel("Time (years)", fontsize='x-small')
Fig4.set_ylabel("Fraction Remaining", fontsize='x-small')
Fig4.set_title("Exponential Decay of Radioactive Elements", fontsize='x-small')
Fig4.legend(loc='upper right')
Fig5.hist(student_grades, bins=10, range=(0,100), edgecolor="black")
Fig5.set_ylim(0,30)
Fig5.set_xlabel("Grades", fontsize='x-small')
Fig5.set_ylabel("Number of Students", fontsize='x-small')
Fig5.set_title("Project A", fontsize='x-small')

# Plotting
## Line Graph
```python
#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

y = np.arange(0, 11) ** 3
x = range(11)
plt.plot(x, y)
```

## Scatter
```python
#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

mean = [69, 0]
cov = [[15, 8], [8, 15]]
np.random.seed(5)
x, y = np.random.multivariate_normal(mean, cov, 2000).T
y += 180

plt.scatter(x, y, c='magenta')
plt.ylabel("Weight (lbs)")
plt.xlabel("Height (in)")
plt.title("Men's Height vs Weight")
plt.show()
```

## Change of Scale
```python
#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 28651, 5730)
r = np.log(0.5)
t = 5730
y = np.exp((r / t) * x)

plt.plot(x, y)
plt.yscale("log")
plt.xlabel("Time (years)")
plt.ylabel("Fraction Remaining")
plt.title("Exponential Decay of C-14")
plt.show()
```

## Two is better than one
```python
#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 21000, 1000)
r = np.log(0.5)
t1 = 5730
t2 = 1600
y1 = np.exp((r / t1) * x)
y2 = np.exp((r / t2) * x)

plt.plot(x,y1, 'r--', label='C-14')
plt.plot(x, y2, 'g', label="Ra-226")
plt.xlabel("Time (years)")
plt.ylabel("Fraction Remaining")
plt.title("Exponential Decay of Radioactive Elements")
plt.legend(loc='upper right')
plt.show()
```

## Frequency
```python
#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

plt.hist(student_grades, bins=10, range=(0,101), edgecolor="black")
plt.ylim(0,30)
plt.xlabel("Grades")
plt.ylabel("Number of Students")
plt.title("Project A")
plt.show()
```

## All in One
```python
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
```

## Stacking Bars
```python
#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4,3))

# Values of each group
a = fruit[0]
b = fruit[1]
o = fruit[2]
p = fruit[3]

# Heights of
bar1 = np.add(a, b).tolist()
bar2 = np.add(bar1, o).tolist()

# The position of the bars on the x-axis
r = [0,1,2]
 
# Names of group and bar width
names = ['Farah','Fred','Felicia']
barWidth = 0.5

# Create apple bars
p1 = plt.bar(r, a, color='red', width=barWidth)
# Create banana bars on top of the firs ones
p2 = plt.bar(r, b, bottom=a, color='yellow', width=barWidth)
# Create oranges bars on top of the second
p3 = plt.bar(r, o, bottom=bar1, color='#ff8000', width=barWidth)
# Create oranges bars on top of the second
p4 = plt.bar(r, p, bottom=bar2, color='#ffe5b4', width=barWidth)

# Custom axis
plt.xticks(r, names)
plt.ylabel("Quantity of Fruit")
plt.title("Number of Fruit per Person")
plt.yticks(np.arange(0, 81, 10))
plt.legend((p1[0], p2[0], p3[0], p4[0]),('apples', 'bananas', 'oranges', 'peaches'))

```

## Gradient
```python
#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)

x = np.random.randn(2000) * 10
y = np.random.randn(2000) * 10
z = np.random.rand(2000) + 40 - np.sqrt(np.square(x) + np.square(y))

marker_size=15
plt.scatter(x, y, marker_size, c=z)
plt.title("Mountain Elevation")
plt.xlabel("x coordinate (m)")
plt.ylabel("y coordinate (m)")
cbar= plt.colorbar()
cbar.set_label("elevation (m)")
```


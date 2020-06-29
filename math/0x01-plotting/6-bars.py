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


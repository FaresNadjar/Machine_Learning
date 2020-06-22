# Linear Algebra
## Slice Me Up 
To slice a list l from x position to y position :```l[x:y]```. It starts at x and ends at y-1. Don't forget that the counters starts from 0 !!

Let's suppose we have a list ```arr = [9, 8, 2, 3, 9, 4, 1, 0, 3]``` and we want to have slices of the list as follows : 

* arr1 should be the first two numbers of arr
* arr2 should be the last five numbers of arr
* arr3 should be the 2nd through 6th numbers of arr

Then here is the code to do it : 

```
#!/usr/bin/env python3
arr = [9, 8, 2, 3, 9, 4, 1, 0, 3]
arr1 = arr[:2]
arr2 = arr[-5:]
arr3 = arr[1:6]
print("The first two numbers of the array are: {}".format(arr1))
print("The last five numbers of the array are: {}".format(arr2))
print("The 2nd through 6th numbers of the array are: {}".format(arr3))
```

## Trim Me Down

Let's suppose we have a 2D matrix, and we want the middle to contain the 3rd and 4th columns of matrix. No conditional statements allowed, only one loop. 

Then here is the code to do it : 

```
#!/usr/bin/env python3
matrix = [[1, 3, 9, 4, 5, 8], [2, 4, 7, 3, 4, 0], [0, 3, 4, 6, 1, 5]]
the_middle = []
for i in matrix: 
	the_middle.append([i[2], i[3]])
print("The middle columns of the matrix are: {}".format(the_middle))
```

## Size Me Please

The best way to know the shape of a matrix is to turn it into a numpy array and takes it shape : 

```
#!/usr/bin/env python3
import numpy as np
def matrix_shape(matrix) : 
	matrix = np.array(matrix)
	return (list(matrix.shape))
```

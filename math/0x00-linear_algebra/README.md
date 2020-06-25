# Linear Algebra
## Slice Me Up 

```python
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

```python
#!/usr/bin/env python3
matrix = [[1, 3, 9, 4, 5, 8], [2, 4, 7, 3, 4, 0], [0, 3, 4, 6, 1, 5]]
the_middle = []
for i in matrix: 
    the_middle.append([i[2], i[3]])
print("The middle columns of the matrix are: {}".format(the_middle))
```

## Size Me Please

```python
#!/usr/bin/env python3
def matrix_shape(matrix):
    shape = [len(matrix)]
    test = matrix[0]
    while (isinstance(test, list)):
        shape.append(len(test))
        test = test[0]
    return (shape)
```

## Flip Me Over

```python
#!/usr/bin/env python3
def matrix_transpose(matrix):
    mat = []
    for i in range(len(matrix[0])):
        mat.append([])
        for j in range(len(matrix)):
            mat[i].append(matrix[j][i])
    return mat
```

## Line Up

```python
#!/usr/bin/env python3
def add_arrays(arr1, arr2):
    if (len(arr1) != len(arr2)):
        return None
    arr = []
    for i in range(len(arr1)):
        arr.append(arr1[i] + arr2[i])
    return (arr)
```

## Across The Planes

```python
#!/usr/bin/env python3
def add_matrices2D(mat1, mat2):
    if (len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0])):
        return None
    mat = []
    for i in range(len(mat1)):
        mat.append([])
        for j in range(len(mat1[0])):
            mat[i].append(mat1[i][j] + mat2[i][j])
    return mat
```

## Howdy Partner

```python
#!/usr/bin/env python3
def cat_arrays(arr1, arr2):
    arr = arr1.copy()
    for i in arr2:
        arr.append(i)
    return arr
```

## Gettin' Cozy 

```python
#!/usr/bin/env python3
def cat_matrices2D(mat1, mat2, axis=0):
    if (axis == 0 and len(mat1[0]) != len(mat2[0])):
        return None
    if (axis == 1 and len(mat1) != len(mat2)):
        return None
    mat = []
    for i in mat1:
        mat.append(i.copy())
    for i in range(len(mat2)):
        if (axis == 0):
            mat.append(mat2[i])
        else:
            for j in mat2[i]:
                mat[i].append(j)
    return mat
```

## Ridin Bareback

```python
#!/usr/bin/env python3
def mat_mul(mat1, mat2):
    if (len(mat1[0]) != len(mat2)):
        return None
    ma t= [[0] for i in range(len(mat1))]
    for i in range(len(mat)):
        mat[i] = [0 for j in range(len(mat2[0]))]
        for j in range(len(mat[0])):
            s = 0
            for k in range(len(mat2)):
                s = s + (mat1[i][k] * mat2[k][j])
            mat[i][j] = s
    return mat
```

## Let The Butcher Slice It

```python
#!/usr/bin/env python3
import numpy as np
matrix = np.array([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12],
                   [13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24]])
mat1 = matrix[1:3]
mat2 = matrix[:, 2:4]
mat3 = matrix[-3:, -3:]
print("The middle two rows of the matrix are:\n{}".format(mat1))
print("The middle two columns of the matrix are:\n{}".format(mat2))
print("The bottom-right, square, 3x3 matrix is:\n{}".format(mat3))
```

## I'll Use My Scale

```python
#!/usr/bin/env python3
def np_shape(matrix):
    return matrix.shape
```

## The Western Exchange

```python
#!/usr/bin/env python3
def np_transpose(matrix):
    new = matrix.transpose()
    return new
```

## Bracin' The Elements
```python
#!/usr/bin/env python3
def np_elementwise(mat1, mat2):
    return (mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2)
```

## Cat's Got Your Tongue
```python
#!/usr/bin/env python3

import numpy as np

def np_cat(mat1, mat2, axis=0):
    new = np.concatenate((mat1, mat2), axis)
    return new
```

## Saddle Up
```python
#!/usr/bin/env python3

import numpy as np

def np_matmul(mat1, mat2):
    new = np.matmul(mat1, mat2)
    return new
```






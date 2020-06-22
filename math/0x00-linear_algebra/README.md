# Linear Algebra
## Slice a list 
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


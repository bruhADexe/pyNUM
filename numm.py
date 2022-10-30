# python numpy library
# numerical python is library used for working with arrays , numpy provide ndarray which are 50 times faster than
# regular python list

import numpy as np

arr = np.array([1, 2, 4, 6])
print(arr)
print(type(arr))

print(np.__version__)
# ndarray from any array like objects such as lists and tuples
arr = np.array((0, 2, 4, 6))
print(arr)
# 3d array
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr)
# prints the dimension
print(arr.ndim)
# array slicing
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[1, 1:4])
# copy method should not be affected by the change made in original array
# while the view() does get affected by the changes made in original array
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr)
print(x)
# Array shaape , returns a tuple with each index having corresponding dimension
# here ndmin is used to create a 5 dimensional array
arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('shape of array :', arr.shape)
# Reshape , changing dims
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(2, 3, 2)

print(newarr)
# Unknown dimension
# reshape(-1) to flatten any multi-dimensional array
print("Unknown Dimension")
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = arr.reshape(1, 2, -1)
print(newarr)



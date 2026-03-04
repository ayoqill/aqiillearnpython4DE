#numpy is use for scientific computing and data analysis.
#It provides support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays efficiently.

import numpy as np

# Create a 1D array
arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)

# Create a 2D array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2)

# Create a 3D array
arr3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(arr3) 

print(arr1.shape) # Output: (5,)
print(arr2.shape) # Output: (2, 3)  
print(arr3.shape) # Output: (2, 2, 2)


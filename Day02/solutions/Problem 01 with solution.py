# Problem 01: Create 2D array [[1,2,3],[4,5,6]]; print array, shape, dtype

# Original Solution
import numpy as np
arr = np.arange(1,7)
arr = arr.reshape(2,3)
print(f"Array :\n{arr}\n Array shape is: {arr.shape} \n Array type is: {arr.dtype}")

# What I learned from your review
"""
I used arange + reshape which is NumPy-idiomatic. Creating with np.array([[1,2,3],[4,5,6]]) is equally valid.
"""

# Updated Solution
import numpy as np
arr = np.arange(1, 7).reshape(2, 3)
print("Array:\n", arr)
print("Shape:", arr.shape)
print("Dtype:", arr.dtype)

# Problem 12: Mean-based replacement: <mean→-5; >mean→5; ==mean unchanged

# Original Solution
import numpy as np
arr = np.array([2, 5, 8, 11, 14, 17, 20])
arr_mean = arr.mean()
arr[arr < arr_mean] = -5
arr[arr > arr_mean] = 5
print(arr)

# What I learned from your review
"""
This was clear; I also learned a concise np.where double-nested pattern for the same result.
"""

# Updated Solution
import numpy as np
arr = np.array([2, 5, 8, 11, 14, 17, 20])
mu = arr.mean()
arr = np.where(arr < mu, -5, np.where(arr > mu, 5, arr))
print(arr)

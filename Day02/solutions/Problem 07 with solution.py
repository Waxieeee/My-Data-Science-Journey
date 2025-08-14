# Problem 07: 1D slicing: evens via slicing; every 3rd starting from 3

# Original Solution
import numpy as np
arr = np.arange(1,21)
even_arr = arr[1::2]
third = arr[2::3]
print(arr, even_arr, third)

# What I learned from your review
"""
Zero-based indexing makes arr[1::2] the evens; arr[2::3] is the 3rd, 6th, 9th, ... values.
"""

# Updated Solution
import numpy as np
arr = np.arange(1, 21)
evens = arr[1::2]
every_third_from_3 = arr[2::3]
print("Evens:", evens)
print("Every 3rd from 3:", every_third_from_3)

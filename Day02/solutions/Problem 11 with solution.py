# Problem 11: 4×5 array 10..29; even→0; odd>20→99

# Original Solution
import numpy as np
arr = np.arange(10,30)
arr[arr %2 == 0] = 0
arr [(arr %2 != 0) & (arr>20) ] = 99
print(arr)

# What I learned from your review
"""
Since I zeroed evens first, the second mask inherently targets odd numbers > 20; an explicit odd-check is fine but not strictly necessary.
"""

# Updated Solution
import numpy as np
A = np.arange(10, 30).reshape(4, 5)
A[A % 2 == 0] = 0
A[(A % 2 == 1) & (A > 20)] = 99
print(A)

# Problem 10: Conditional assignment: 1..20; 5..15 inclusive; set <10 to -1 (in-place)

# Original Solution
import numpy as np
arr = np.arange(1,21)
mask = (arr > 5) & (arr<=15)
masked_arr = arr[mask]
masked_arr[masked_arr<10] = -1
print(masked_arr)

# What I learned from your review
"""
I learned arr[mask] returns a copy; to modify original, combine masks directly in one index expression.
"""

# Updated Solution
import numpy as np
arr = np.arange(1, 21)
arr[(arr >= 5) & (arr <= 15) & (arr < 10)] = -1
print(arr)

# Problem 09: Boolean indexing: select values >10 and <18

# Original Solution
import numpy as np
arr_1d = np.array([2, 5, 8, 11, 14, 17, 20])
mask = (arr_1d >10) & (arr_1d < 18)
print(arr_1d[mask])

# What I learned from your review
"""
Chaining with & and parentheses is the correct pattern to avoid precedence issues.
"""

# Updated Solution
import numpy as np
arr_1d = np.array([2, 5, 8, 11, 14, 17, 20])
sel = arr_1d[(arr_1d > 10) & (arr_1d < 18)]
print(sel)

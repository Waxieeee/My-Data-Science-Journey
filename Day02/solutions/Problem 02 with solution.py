# Problem 02: Array from 10 to 30 inclusive with step 5 (arange)

# Original Solution
import numpy as np
spaced_arr = np.arange(10,31,5)
print(spaced_arr)

# What I learned from your review
"""
`arange` stop is exclusive unless the sequence lands exactly on it, which it does here (30).
"""

# Updated Solution
import numpy as np
spaced_arr = np.arange(10, 31, 5)
print(spaced_arr)

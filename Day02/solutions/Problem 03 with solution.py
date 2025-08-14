# Problem 03: 7 evenly spaced numbers between 5 and 50 (linspace)

# Original Solution
import numpy as np
arr1 = np.linspace(5,50,7)
print(arr1)

# What I learned from your review
"""
`linspace` is great when I know how many points I want rather than the step size.
"""

# Updated Solution
import numpy as np
arr1 = np.linspace(5, 50, 7)
print(arr1)
print("Step size:", arr1[1] - arr1[0])

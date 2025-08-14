# Problem 04: Sine of 100 points from 0 to 2π

# Original Solution
import numpy as np
sine = np.sin(np.linspace(0 , 2*np.pi, 100))
print(sine)

# What I learned from your review
"""
I learned it’s clearer to store x-values, but passing linspace directly to np.sin is still vectorized and fine.
"""

# Updated Solution
import numpy as np
x = np.linspace(0, 2*np.pi, 100)
sine = np.sin(x)
print("First 5:", sine[:5])

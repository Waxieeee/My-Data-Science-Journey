# Problem 06: Sine of 200 points 0→4π; reshape 20×10; first 5, shape, mean, std

# Original Solution
import numpy as np
arr = np.linspace(0 , 4*np.pi, 200)
sine_values = np.sin(arr)
re_sin = sine_values.reshape(20,10)
print(f"First 5 sine values: {sine_values[:5]}")
print(f"Shape of the reshaped sine array: {re_sin.shape}")
mean = np.mean(sine_values)
print(f"Mean deviation of all sine values: {mean}")
stand = np.std(sine_values)
print(f"Standard deviation of all sine values: {stand}")

# What I learned from your review
"""
I corrected my prints to slice the original sine array for the first 5 values and acknowledged that reshaping doesn’t affect stats.
"""

# Updated Solution
import numpy as np
x = np.linspace(0, 4*np.pi, 200)
sine_values = np.sin(x)
sine_matrix = sine_values.reshape(20, 10)
print("First 5:", sine_values[:5])
print("Shape:", sine_matrix.shape)
print("Mean:", sine_values.mean(), "Std:", sine_values.std())

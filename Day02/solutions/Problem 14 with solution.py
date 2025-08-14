# Problem 14: Mixed slicing + broadcasting quiz: verify shapes/values

# Original Solution
# I predicted outputs; now verify programmatically.

# What I learned from your review
"""
I validated A*B (broadcast across rows), A*C (down columns), A[1:,2:], and paired selection A[[0,2],[1,3]].
"""

# Updated Solution
import numpy as np
A = np.arange(1, 13).reshape(3, 4)
B = np.array([10, 20, 30, 40])
C = np.array([[1],[2],[3]])

print("A:\n", A)
print("A[1:,2:] ->\n", A[1:, 2:])
print("A*B ->\n", A * B)
print("A*C ->\n", A * C)
print("A[[0,2],[1,3]] ->", A[[0,2],[1,3]])
print("A[np.ix_([0,2],[1,3])] ->\n", A[np.ix_([0,2],[1,3])])

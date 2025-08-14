# Problem 15: Broadcasting check: A*B, A*C, and B*C outer product

# Original Solution
# I initially thought B*C might fail; learned it works and yields a (3,3) outer product.

# What I learned from your review
"""
`B` behaves like shape (1,3) and `C` like (3,1), so broadcasting yields (3,3).
"""
import numpy as np

# Updated Solution
import numpy as np
A = np.array([[1,2,3],[4,5,6],[7,8,9]])
B = np.array([1,2,3])
C = np.array([[1],[2],[3]])

print("A*B ->\n", A*B)
print("A*C ->\n", A*C)
print("B*C (outer) ->\n", B*C)
print("Shapes:", (A*B).shape, (A*C).shape, (B*C).shape)

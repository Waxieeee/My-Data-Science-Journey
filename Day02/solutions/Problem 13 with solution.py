# Problem 13: Fancy indexing drill: pairing vs rectangles

# Original Solution
# Predictions noted in chat; verified outputs below in updated solution.

# What I learned from your review
"""
I confirmed that [rows, cols] of same length selects pairs; to get a rectangle from row/col lists I should use np.ix_. Boolean mask over 2D returns a flattened 1D list of matches.
"""

# Updated Solution
import numpy as np
M = np.arange(1, 13).reshape(3, 4)
print("M:\n", M)
print("Pairs M[[0,2],[1,3]] ->", M[[0,2],[1,3]])              # [ 2 12]
print("Rows+slice M[[0,2],1:] ->\n", M[[0,2], 1:])            # [[2 3 4],[10 11 12]]
print("Rect via ix M[np.ix_([0,2],[1,3])] ->\n", M[np.ix_([0,2],[1,3])])
mask3 = M % 3 == 0
print("Mask ==0 mod3 ->", M[mask3])                           # [3 6 9 12]
row_mask = [True, False, True]; col_mask = [False, True, True, False]
print("Row+col masks ->\n", M[row_mask, :][:, col_mask])      # [[2 3],[10 11]]

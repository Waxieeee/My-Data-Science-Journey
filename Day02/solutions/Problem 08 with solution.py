# Problem 08: 2D slicing: 3×5 10..24; first 2 rows last 3 cols; last row reversed

# Original Solution
import numpy as np
arr_2 = np.arange(10,25)
shaped = arr_2.reshape(3,5)
slice = shaped[0:2,-3:]
last_row = shaped[-1]
last_row_rev = last_row[::-1]
print (f"Array: \n\n {arr_2} \n")
print (f"Array Shaped 3x5: \n\n  {shaped}\n")
print (f"First 2 rows, last 2 columns:\n\n {slice}\n")
print (f"Last row reveresed : \n\n  {last_row_rev}\n")

# What I learned from your review
"""
I mislabeled the text as last 2 columns but sliced last 3 correctly. Reverse slicing row-wise with ::-1 is idiomatic.
"""

# Updated Solution
import numpy as np
A = np.arange(10, 25).reshape(3, 5)
last3cols_first2rows = A[:2, -3:]
last_row_reversed = A[-1, ::-1]
print("Matrix:\n", A)
print("First 2 rows, last 3 cols:\n", last3cols_first2rows)
print("Last row reversed:\n", last_row_reversed)

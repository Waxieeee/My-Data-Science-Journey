# Problem 05: 20 numbers 10→100; reshape 4×5; print step, mean, std

# Original Solution
import numpy as np
arr = np.linspace(10,100,20)
arr_final = arr.reshape(4,5)
# diff = arr[0] - arr[1]
diff = np.diff(arr)[15]  # NumPy way
print(arr_final, diff, np.mean(arr), np.std(arr))

# What I learned from your review
"""
I mistakenly grabbed a later diff index; since spacing is uniform, any works, but conventionally I should use np.diff(arr)[0] or arr[1]-arr[0].
"""

# Updated Solution
import numpy as np
arr = np.linspace(10, 100, 20)
arr_final = arr.reshape(4, 5)
step = np.diff(arr)[0]
print("4x5 array:\n", arr_final)
print("Step:", step)
print("Mean:", arr.mean(), "Std:", arr.std())

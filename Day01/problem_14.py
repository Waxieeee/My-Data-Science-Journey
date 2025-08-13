# Problem 14: Create NumPy array (1–16), reshape to 4x4, get attributes
import numpy as np
new_list = np.arange(1, 17)
reshaped_list = new_list.reshape(4, 4)
print("Shape:", reshaped_list.shape)
print("Dimensions:", reshaped_list.ndim)
print("Data type:", reshaped_list.dtype)
print("Size:", reshaped_list.size)
updated_type = reshaped_list.astype(float)
print("Converted Data type:", updated_type.dtype)

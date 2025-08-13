# Problem 13: Convert list of [name, number] pairs to dictionary with value squared
data = [["Alice", 25], ["Bob", 30], ["Charlie", 35]]
data_dict = {i: x**2 for i, x in data}
print(data_dict)

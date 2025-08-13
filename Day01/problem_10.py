# Problem 10: Flatten a matrix using list comprehension
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [i for row in matrix for i in row]
print(flat)

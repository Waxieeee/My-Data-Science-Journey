# Problem 11: Nested comprehension - transform even numbers (square) and odd numbers (double)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat_transform = [i**2 if i % 2 == 0 else i*2 for row in matrix for i in row]
print(flat_transform)

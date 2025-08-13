# Problem 12: Generate Cartesian product of (x, y) where (x+y) is even
pairs = [(x, y) for x in range(4) for y in range(4) if (x+y) % 2 == 0]
print(pairs)

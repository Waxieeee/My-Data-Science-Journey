# Problem 1: Filter even numbers from a list
a = [1, 2, 3, 4, 5, 6]

# Solution
evens = []
for i in a:
    if i % 2 == 0:
        evens.append(i)
print(evens)

# Updated Solution
evens = [i for i in a if i % 2 == 0]
print(evens)

# Problem 7: List comprehension - words longer than 3 letters
words = ["this", "is", "a", "test"]
final = [i for i in words if len(i) > 3]
print(final)

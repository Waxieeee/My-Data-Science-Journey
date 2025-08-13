# Problem 2: Filter dictionary items where value > 75
scores = {"Alice": 80, "Bob": 70, "Charlie": 90}

# Solution
high_score = {}
for i, x in scores.items():
    if x > 75:
        high_score[i] = x
print(high_score)

# Updated Solution
high_score = {name: score for name, score in scores.items() if score > 75}
print(high_score)

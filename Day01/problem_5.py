# Problem 5: Get names starting with "a" and convert to uppercase
names = ["alex", "bob", "anna", "mike"]

# Solution
a_names = []
for i in names:
    if i.startswith("a"):
        a_names.append(i.upper())
print(a_names)

# Updated Solution
a_names = [name.upper() for name in names if name.startswith("a")]
print(a_names)

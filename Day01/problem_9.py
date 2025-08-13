# Problem 9: Dict comprehension - names mapped to their lengths (uppercase keys)
names = ["alex", "bob", "anna", "mike"]
name_dict = {i.upper(): len(i) for i in names}
print(name_dict)

# Curly braces { } with values = set
colours = {"red", "blue", "green"}

# Duplicates removed automatically!
tags = {"python", "coding", "python", "tutorial", "coding"}
print(tags)  # {'python', 'coding', 'tutorial'} — 3 unique items

# Convert a list → set to deduplicate instantly
votes = ["Alice", "Bob", "Alice", "Carol", "Bob"]
unique = set(votes)
tuple=tuple(votes)
print(unique)  # {'Alice', 'Bob', 'Carol'}
print(tuple)
print(tuple[0])

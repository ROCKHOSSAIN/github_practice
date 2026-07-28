candidates = [
    {"name": "Alice",  "age": 28, "experience": 4},
    {"name": "Bob",    "age": 21, "experience": 1},
    {"name": "Carol",  "age": 35, "experience": 8},
    {"name": "Dave",   "age": 19, "experience": 0},
    {"name": "Eve",    "age": 30, "experience": 3},
]
eligible=list(filter(lambda c:c["age"]>=23 and c["experience"]>=3,candidates))
for c in eligible:
    print(f"  {c['name']} | Age: {c['age']} | Exp: {c['experience']} yrs")

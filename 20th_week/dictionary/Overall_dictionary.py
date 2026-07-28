# ===========================
# Python Dictionary (Basic)
# ===========================

# Dictionary = key : value pair
# Syntax:
# {key: value}

student = {
    "name": "Rocky",
    "age": 24,
    "country": "Japan"
}

print(student)


# -----------------------------------
# 1. Value Access (Value বের করা)
# -----------------------------------

print(student["name"])      # Rocky
print(student["age"])       # 24

# get() ব্যবহার করলে key না থাকলেও error হবে না
print(student.get("country"))    # Japan
print(student.get("phone"))      # None
print(student.get("score","N/A"))# N/A jokhon key thakbe na


# -----------------------------------
# 2. New Key Add (নতুন data যোগ করা)
# -----------------------------------

student["phone"] = "09012345678"

print(student)


# -----------------------------------
# 3. Value Update (ডাটা পরিবর্তন)
# -----------------------------------

student["age"] = 25

print(student)


# -----------------------------------
# 4. Delete Data (ডাটা মুছে ফেলা)
# -----------------------------------

del student["phone"]

print(student)

# pop()
student.pop("country")

print(student)


# -----------------------------------
# 5. Length (কতগুলো key আছে)
# -----------------------------------

print(len(student))


# -----------------------------------
# 6. Check Key Exists
# -----------------------------------

print("name" in student)      # True
print("phone" in student)     # False


# -----------------------------------
# 7. Loop Dictionary
# -----------------------------------

# শুধু key

for key in student:
    print(key)

# Output
# name
# age


# -----------------------------------
# 8. Loop Values
# -----------------------------------

for value in student.values():
    print(value)

# Output
# Rocky
# 25


# -----------------------------------
# 9. Loop Key & Value
# -----------------------------------

for key, value in student.items():
    print(key, value)

# Output
# name Rocky
# age 25


# -----------------------------------
# 10. Nested Dictionary
# -----------------------------------

school = {
    "s1": {
        "name": "Alice",
        "grade": "A"
    },
    "s2": {
        "name": "Bob",
        "grade": "B"
    }
}

print(school["s1"]["name"])     # Alice

for sid, info in school.items():
    print(sid)
    print(info["name"])
    print(info["grade"])


# -----------------------------------
# 11. Dictionary Copy
# -----------------------------------

student2 = student.copy()

print(student2)


# -----------------------------------
# 12. Clear Dictionary
# -----------------------------------

student.clear()

print(student)      # {}


# -----------------------------------
# 13. Dictionary from Scratch
# -----------------------------------

person = {}
person["name"] = "Alif"
person["age"] = 23

print(person)


# -----------------------------------
# 14. Mixed Data Type
# -----------------------------------

data = {
    "name": "Rocky",
    "age": 24,
    "isStudent": True,
    "marks": [90, 85, 80]
}

print(data["marks"])
print(data["marks"][0])


# -----------------------------------
# 15. Dictionary Inside List
# -----------------------------------

students = [
    {"name": "Alice", "grade": "A"},
    {"name": "Bob", "grade": "B"},
    {"name": "John", "grade": "A+"}
]

for student in students:
    print(student["name"], student["grade"])


# ===================================
# যেগুলো করা যায় (✓)
# ===================================

# ✓ Add
# ✓ Update
# ✓ Delete
# ✓ Search
# ✓ Loop
# ✓ Nested Dictionary
# ✓ Store list
# ✓ Store another dictionary
# ✓ Count using len()


# ===================================
# যেগুলো করা যায় না (✗)
# ===================================

# ✗ Duplicate key রাখা যায় না

d = {
    "name": "Alice",
    "name": "Bob"
}

print(d)
# Output:
# {'name': 'Bob'}
# শেষের value টা থাকবে।


# ✗ Index দিয়ে access করা যায় না

student = {
    "name": "Rocky",
    "age": 24
}

# print(student[0])   # Error


# ✗ Slice করা যায় না

# print(student[0:2])   # Error


# ===================================
# সবচেয়ে গুরুত্বপূর্ণ Methods
# ===================================

student = {
    "name": "Rocky",
    "age": 24
}

print(student.keys())      # সব key
print(student.values())    # সব value
print(student.items())     # key,value pair
print(student.get("name"))
print(student.pop("age"))
student.clear()
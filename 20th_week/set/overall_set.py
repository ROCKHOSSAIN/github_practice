# ============================
# Python Set (Basic)
# ============================

# Set তৈরি
fruits = {"Apple", "Banana", "Mango"}

print(fruits)


# -----------------------------------
# 1. Add Item
# -----------------------------------

fruits.add("Orange")

print(fruits)


# -----------------------------------
# 2. Multiple Item Add
# -----------------------------------

fruits.update(["Grapes", "Pineapple"])
print(fruits)


# -----------------------------------
# 3. Remove Item
# -----------------------------------

fruits.remove("Banana")

print(fruits)

# remove() দিলে item না থাকলে Error হবে


# -----------------------------------
# 4. discard()
# -----------------------------------

fruits.discard("Jackfruit")

print(fruits)

# discard() দিলে item না থাকলেও Error হবে না


# -----------------------------------
# 5. pop()
# -----------------------------------

item = fruits.pop()

print(item)
print(fruits)

# Set unordered তাই কোন item delete হবে আগে থেকে জানা যায় না


# -----------------------------------
# 6. Length
# -----------------------------------

print(len(fruits))


# -----------------------------------
# 7. Search
# -----------------------------------

print("Apple" in fruits)
print("Banana" in fruits)


# -----------------------------------
# 8. Loop
# -----------------------------------

for item in fruits:
    print(item)


# -----------------------------------
# 9. Copy
# -----------------------------------

set1 = {1,2,3}

set2 = set1.copy()

print(set2)


# -----------------------------------
# 10. Clear
# -----------------------------------

set1.clear()

print(set1)


# -----------------------------------
# 11. Empty Set
# -----------------------------------

numbers = set()

numbers.add(10)
numbers.add(20)

print(numbers)


# -----------------------------------
# 12. Duplicate Automatically Remove
# -----------------------------------

nums = {1,2,2,2,3,4,4,5}

print(nums)

# Output
# {1,2,3,4,5}


# -----------------------------------
# 13. Union
# -----------------------------------

a = {1,2,3}
b = {3,4,5}

print(a.union(b))

# Output
# {1,2,3,4,5}


# -----------------------------------
# 14. Intersection
# -----------------------------------

a = {1,2,3}
b = {2,3,4}

print(a.intersection(b))

# Output
# {2,3}


# -----------------------------------
# 15. Difference
# -----------------------------------

a = {1,2,3}
b = {2,3,4}

print(a.difference(b))

# Output
# {1}


# -----------------------------------
# 16. Symmetric Difference
# -----------------------------------

a = {1,2,3}
b = {2,3,4}

print(a.symmetric_difference(b))

# Output
# {1,4}


# ===================================
# যেগুলো করা যায়
# ===================================

# Add
# Remove
# Search
# Loop
# Copy
# Clear
# Union
# Intersection
# Difference
# Symmetric Difference


# ===================================
# যেগুলো করা যায় না
# ===================================

# Duplicate রাখা যায় না
# Index নেই
# Slicing করা যায় না
# Update by index করা যায় না
# Ordered না
# items() নেই
# keys() নেই
# values() নেই


# ===================================
# সবচেয়ে গুরুত্বপূর্ণ Methods
# ===================================

# add()
# update()
# remove()
# discard()
# pop()
# clear()
# copy()
# union()
# intersection()
# difference()
# symmetric_difference()
# len()


# ===================================
# Important Notes
# ===================================

# {} = Empty Dictionary

empty_dict = {}

print(type(empty_dict))

# Output:
# <class 'dict'>


# Empty Set

empty_set = set()

print(type(empty_set))

# Output:
# <class 'set'>
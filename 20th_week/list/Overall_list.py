# ============================
# Python List (Basic)
# ============================

# List তৈরি
fruits = ["Apple", "Banana", "Mango"]

print(fruits)


# -----------------------------------
# 1. Value Access
# -----------------------------------

print(fruits[0])
print(fruits[2])

# Negative Index
print(fruits[-1])


# -----------------------------------
# 2. Slice
# -----------------------------------

print(fruits[0:2])
print(fruits[:2])
print(fruits[1:])


# -----------------------------------
# 3. Add Item
# -----------------------------------

fruits.append("Orange")

print(fruits)


# -----------------------------------
# 4. Insert Item
# -----------------------------------

fruits.insert(1, "Grapes")

print(fruits)


# -----------------------------------
# 5. Update Item
# -----------------------------------

fruits[0] = "Pineapple"

print(fruits)


# -----------------------------------
# 6. Delete Item
# -----------------------------------

fruits.remove("Banana")

print(fruits)

fruits.pop()

print(fruits)

del fruits[0]

print(fruits)


# -----------------------------------
# 7. Length
# -----------------------------------

print(len(fruits))


# -----------------------------------
# 8. Search
# -----------------------------------

print("Mango" in fruits)
print("Apple" in fruits)


# -----------------------------------
# 9. Index
# -----------------------------------

fruits = ["Apple", "Banana", "Mango"]

print(fruits.index("Banana"))


# -----------------------------------
# 10. Count
# -----------------------------------

numbers = [1,2,2,2,3,4]

print(numbers.count(2))


# -----------------------------------
# 11. Sort
# -----------------------------------

numbers = [5,1,8,2]

numbers.sort()

print(numbers)


# -----------------------------------
# 12. Reverse
# -----------------------------------

numbers.reverse()

print(numbers)


# -----------------------------------
# 13. Loop
# -----------------------------------

for item in fruits:
    print(item)


# -----------------------------------
# 14. Loop with Index
# -----------------------------------

for i, value in enumerate(fruits):
    print(i, value)


# -----------------------------------
# 15. Nested List
# -----------------------------------

marks = [
    [80,90],
    [70,60]
]

print(marks[0][1])


# -----------------------------------
# 16. Extend
# -----------------------------------

a = [1,2]
b = [3,4]

a.extend(b)

print(a)


# -----------------------------------
# 17. Copy
# -----------------------------------

list1 = [10,20,30]

list2 = list1.copy()

print(list2)


# -----------------------------------
# 18. Clear
# -----------------------------------

list1.clear()

print(list1)


# -----------------------------------
# 19. Empty List
# -----------------------------------

names = []

names.append("Alif")
names.append("Rocky")

print(names)


# ===================================
# করা যায়
# ===================================

# Add
# Update
# Delete
# Search
# Sort
# Reverse
# Slice
# Copy
# Loop
# Nested List


# ===================================
# করা যায় না
# ===================================

# Duplicate বন্ধ করা যায় না
# Key দিয়ে Access করা যায় না
# items() নেই
# keys() নেই
# values() নেই


# ===================================
# গুরুত্বপূর্ণ Method
# ===================================

# append()
# insert()
# remove()
# pop()
# clear()
# copy()
# extend()
# sort()
# reverse()
# count()
# index()
# len()
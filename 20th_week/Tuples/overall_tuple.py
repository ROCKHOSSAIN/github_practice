# ============================
# Python Tuple (Basic)
# ============================

# Tuple তৈরি
fruits = ("Apple", "Banana", "Mango")

print(fruits)


# -----------------------------------
# 1. Access Value
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
# 3. Length
# -----------------------------------

print(len(fruits))


# -----------------------------------
# 4. Search
# -----------------------------------

print("Apple" in fruits)
print("Orange" in fruits)


# -----------------------------------
# 5. Loop
# -----------------------------------

for item in fruits:
    print(item)


# -----------------------------------
# 6. Loop with Index
# -----------------------------------

for i, value in enumerate(fruits):
    print(i, value)


# -----------------------------------
# 7. Count
# -----------------------------------

numbers = (1,2,2,3,2)

print(numbers.count(2))#



# -----------------------------------
# 8. Index
# -----------------------------------

numbers = (10,20,30,40)

print(numbers.index(30))


# -----------------------------------
# 9. Nested Tuple
# -----------------------------------

marks = (
    (80,90),
    (70,60)
)

print(marks[0][1])


# -----------------------------------
# 10. Tuple Packing
# -----------------------------------

person = ("Alif",23,"Japan")

print(person)


# -----------------------------------
# 11. Tuple Unpacking
# -----------------------------------

name, age, country = person

print(name)
print(age)
print(country)


# -----------------------------------
# 12. Copy
# -----------------------------------

t1 = (1,2,3)

t2 = t1

print(t2)

# Tuple immutable তাই copy() method নেই


# ===================================
# যেগুলো করা যায়
# ===================================

# Access
# Search
# Slice
# Loop
# Count
# Index
# Nested Tuple
# Packing
# Unpacking
# len()


# ===================================
# যেগুলো করা যায় না
# ===================================

# Add করা যায় না
# Update করা যায় না
# Remove করা যায় না
# append() নেই
# insert() নেই
# remove() নেই
# pop() নেই
# clear() নেই
# copy() নেই
# sort() নেই
# reverse() নেই


# ===================================
# নিচেরগুলো Error দিবে
# ===================================

fruits = ("Apple","Banana","Mango")

# fruits.append("Orange")      # Error
# fruits.insert(1,"Orange")    # Error
# fruits.remove("Banana")      # Error
# fruits.pop()                 # Error
# fruits.clear()               # Error

# fruits[0] = "Orange"         # Error

# del fruits[0]                # Error


# পুরো Tuple delete করা যায়

del fruits

# print(fruits)    # Error


# ===================================
# Duplicate Allowed
# ===================================

nums = (1,2,2,2,3)

print(nums)


# ===================================
# Mixed Data Type
# ===================================

data = ("Alif",23,True,3.14)

print(data)


# ===================================
# One Item Tuple
# ===================================

a = (10,)

print(type(a))

# এটা Tuple


b = (10)

print(type(b))

# এটা int


# ===================================
# সবচেয়ে গুরুত্বপূর্ণ Functions/Methods
# ===================================

# len()
# count()
# index()
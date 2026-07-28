fruits = {"apple", "banana"}

fruits.add("cherry")       # add one item
fruits.update(["mango", "grape"])  # add multiple

fruits.remove("banana")    # error if missing! the key
fruits.discard("pineapple") # safe — no error if missing ✓ the key

# Membership check — blazing fast even with millions of items!
if "apple" in fruits:
    print("Found it!")
print(fruits)

# or --set e eta kora possible na

# colors = {"red", "blue"}

# colors[0] = "green"
my_tuple = (1, 2, 3)
temp=list(my_tuple)
temp.remove(2)
# print(temp)
updated_tuple=tuple(temp)
print(updated_tuple)

# tuple ke sorasori change kora jay na,eijnno list e convert korar por abar tuple e convert kore nia asha lage

# tuple e add korar process
my_tuple2 = (1, 2, 3)
new_tuple=my_tuple+(4,)
print(new_tuple)

# or 
thistuple1 = ("apple", "banana", "cherry")
# Add tuple to a tuple one or  many 
y = ("orange","guava",)
thistuple1 += y

print(thistuple1)


# or 
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)



# or 

thistuple2 = ("apple", "banana")
del thistuple2
print(thistuple2)



# Tuple immutable। তাই সরাসরি:
# ❌ Update করা যায় না
# ❌ Add করা যায় না
# ❌ Remove/Delete item করা যায় না
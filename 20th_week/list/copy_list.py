thislist = ["apple", "banana", "cherry"]
# copy
mylist=list(thislist)
mylist.append("orange");
print(thislist)
print(mylist)


# 2nd way to copy

another_list=thislist.copy()
print(another_list)

# 3rd way
new_fruits = thislist[:]
print(new_fruits)
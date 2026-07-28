# The union() and update() methods joins all items from both sets.

# The intersection() method keeps ONLY the duplicates.

# The difference() method keeps the items from the first set that are not in the other set(s).

# The symmetric_difference() method keeps all items EXCEPT the duplicates.

# union

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

# set3=set1.union(set2)
set3 = set1 | set2

print(set3)

# intersection
set11 = {"apple", "banana", "cherry"}
set22 = {"google", "microsoft", "apple"}

# set33 = set11 & set22
set3 = set11.intersection(set22)

print(set3)

# difference
set111 = {"apple", "banana", "cherry"}
set222 = {"google", "microsoft", "apple"}

# set3 = set1 - set2
set333 = set111.difference(set222)
print(set333)
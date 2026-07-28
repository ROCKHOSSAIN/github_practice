# List (Mutable = change করা যায়)
my_list = [1, 2, 3]
my_list[0] = 100

# Tuple (Immutable = change করা যায় না)
my_tuple = (1, 2, 3)
# my_tuple[0] = 100   # Error হবে

# Set (Mutable, কিন্তু index নেই)
my_set = {1, 2, 3}
my_set.add(100)

print("List :", my_list)
print("Tuple:", my_tuple)
print("Set  :", my_set)

# Conversion
print("\nConversions:")
print("List -> Tuple:", tuple(my_list))
print("List -> Set:", set(my_list))

print("Tuple -> List:", list(my_tuple))
print("Tuple -> Set:", set(my_tuple))

print("Set -> List:", list(my_set))
print("Set -> Tuple:", tuple(my_set))
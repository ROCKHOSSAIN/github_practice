fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

# or
# * to the variable name and the values will be assigned to the variable as a list
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(g,y,*r)=fruits
print(g)
print(y)
print(r)

# or 

fruits1 = ("apple", "banana", "cherry", "strawberry", "raspberry")
(g,*y,r)=fruits1
print(g)
print(y)
print(r)
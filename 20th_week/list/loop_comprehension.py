# squares=[]
# for x in range(5):
#     squares.append(x)
# print(squares)


#eta comprehension process 
square=[x for x in range(5)]
print(square)

# another way 

[print(x) for x in ['apple', 'banana', 'cherry']]

# conditions
[print(x) for x in [1,2,3,4,5] if x%2==0]

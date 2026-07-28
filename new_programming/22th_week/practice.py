new_list=[]
val=int(input("enter val"))
# for i in range(val):
#     print(i ** 2)
for i in range(val):
    if(i%2==0):
        new_list.append(i**2)
for i in new_list:
    print(i)


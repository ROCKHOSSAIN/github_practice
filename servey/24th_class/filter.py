# def is_even(n):return n%2==0

new_list=list(filter(lambda p:p%2==0,[1,2,3,4,5]))
print(new_list)

# or
def is_even(n):return n%2==0

new_list2=list(filter(is_even,[1,2,3,4,5,6,7,8,9]))
print(new_list2)

# or filter falsy value 

new_list3=list(filter(None,["",0,False,1,True,""]))
print(new_list3)
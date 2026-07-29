x=1
y=1
z=1
n=2
# x=1
# y=1
# z=2
# n=3
# n=solveing
all_list=[]
new_list=[]
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            all_list.append([i,j,k])
            if(i+j+k!=n):
                new_list.append([i,j,k])

print(all_list)
print(new_list)

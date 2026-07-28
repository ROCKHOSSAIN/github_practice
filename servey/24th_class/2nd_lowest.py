list_student=[]
new_list=[]
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list_student.append([name,score])
lst = sorted(list_student, key=lambda l: l[1], reverse=None)
# lst=sorted(list_student,key=lambda l:l[1],reverse=None)
# for i,s in enumerate(lst):
#     print(s[i])
for i in range(len(lst)+1):
    print(i[-2])
    print(i[1])
    # if(i[-2]==i[1]):
    #     new_list.append([i[0],i[1]])
        
# print(new_list)
# print()

# print(lst)

# list_student.sort()
# highest=list_student[0]
# for i,s in enumerate(list_student,1):
#     print(f"{i}->{s}")
#     if(list_student[i]<highest):
#         highest=list_student[i]


# print(list_student.sort())

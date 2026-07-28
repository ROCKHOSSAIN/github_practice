students = ["Alice", "Bob", "Carol"]
for student in students:
    print(f"hello{student}")

for index,value in enumerate(students):
    print(f"{index+1}->{value}")
# another way of looping through list
for i in range(len(students)):
    print(students[i])
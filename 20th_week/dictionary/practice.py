student = {
    "name": "Rocky",
    "age": 24,
    "country": "Japan"
}
student["scl"]="armanitola"
student["age"]=26
# student.popitem()
# print(student["age"].index())
for key in student.keys():
    print(key)
for value in student.values():
    print(value)
student1=student.copy()

print(student)
print(student1)

person ={}

person["name"]="Alif"
person["age"]=23
print(person)
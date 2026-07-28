# student = {"name": "Aiko", "age": 22, "grade": "A"}
# for key in student:
#     print(key)
# for value in student.values():
#     print(value)

# for key,value in student.items():
#     print(f"{key}: {value}")

# another 

school = {
    "s1": {"name": "Alice", "grade": "A"},
    "s2": {"name": "Bob",   "grade": "B"},
}
print(school["s1"]["name"])
# ekhane info bolte name ,grade egula bujhache
for sid, info in school.items():
    print(f"{sid}->{info['name']} got {info['grade']}")

# or  

# for key, value in school.items():
#     print(f"{key} -> {value['name']} got {value['grade']}") 
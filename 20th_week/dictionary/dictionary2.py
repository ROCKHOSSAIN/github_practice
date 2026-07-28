student = {"name": "Aiko", "age": 22, "grade": "A"}

removed = student.pop("grade")  # remove key, return value → "A"
del student["age"]               # delete by key
student.popitem()                 # remove last inserted pair
student.clear()  
# print(removed)                 # wipe everything → {}
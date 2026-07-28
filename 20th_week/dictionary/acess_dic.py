car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x=car.keys()
print(x)
car["color"]="white"
for key,value in car.items():
    print(f"{key}->{value}")
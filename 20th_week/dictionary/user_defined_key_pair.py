person = {}

n = int(input("How many properties? "))

for i in range(n):
    key = input("Enter key: ")

    if key == "done":
        break

    value = input("Enter value: ")

    if key in person:
        print("Don't give same key")
    else:
        person[key] = value

print(person)
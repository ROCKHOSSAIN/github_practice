def divide(num1, num2):
    if num1 % num2 == 0:
        return num1 // num2

num1 = int(input("enter number 1: "))
num2 = int(input("enter number 2: "))

result = divide(num1, num2)
print(result)
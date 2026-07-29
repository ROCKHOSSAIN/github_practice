def decorator(func):
    def wrapper():
        print("transaction inititated")
        func()
        print("transaction completed")
    return wrapper

@decorator
def hello():
    print("executing all steps of transaction")
hello()
# def hello():
#      print("executing all steps of transaction")

# hello1=decorator(hello)
# print(hello1())


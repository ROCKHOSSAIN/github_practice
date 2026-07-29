def decorator(func):
    def wrapper():
        print("transaction initiated")
        func()
        print("transaction completed")
        # wrapper  er nijesso kisui return hocche na
        # return "wrapper"
    return wrapper
# decorator only returning wrapper function
def hello():
    print("executing all steps of transaction")
hello1=decorator(hello)
hello1()
# hello1=wrapper
# print(hello1())
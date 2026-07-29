def outer():
    msg="i king"
    def inner():
        print(msg)
    return inner
my_function=outer()
my_function()
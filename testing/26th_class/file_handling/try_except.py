try:
    with open("my.txt","r") in file:
        print(file.read())
except FileNotFoundError:
    print("the file isnt existed")
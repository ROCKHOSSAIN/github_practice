def create_profile(**details):
    for key,value in details.items():
        print(f"{key}->{value}")


create_profile(name="Rocky", age=25,city="osaka",role="engineer")
# or 

# যত খুশি keyword arguments dictionary আকারে গ্রহণ করা।
# def student(**info):
#     print(info)

# result=student(name="Rocky", age=25)
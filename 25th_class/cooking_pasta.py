import time
def log_and_time(func):
    def wrapper():
        start=time.time()
        func()
        end=time.time()
        ellapsed=start-end
        print(f"finished time {ellapsed}")
    return wrapper
# def cook_paste():
#     print("nice cooking")
# res=log_and_time(cook_paste)
# print(res())
@log_and_time
def cook_paste():
    print("nice cooking")
cook_paste()

    
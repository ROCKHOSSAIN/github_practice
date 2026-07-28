total=0
with open("study_log.txt","r") as file:
    for line in file:
        name,price=line.split(",")
        total+=int(price)

print("TOTAL PRICE:",total)
items=["onigiri\n","green\n","umbrella\n","mobile"]

with open("shopping_cart","w") as file:
    file.writelines(items)
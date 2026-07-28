
def list_product(product_name, price, **specs):
    print(f"{product_name}->{price}")
    for key,value in specs.items():
        print(f"{key}=>{value}")
    print()
    print("-------------")

list_product("Laptop", 65000,
  brand="Dell", ram="16GB",
  storage="512GB SSD")

list_product("T-Shirt", 799,
  colour="Navy", size="L",
  material="Cotton")
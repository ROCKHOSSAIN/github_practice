def place_order(order,size="medium",sauce=False):
#    "Yes" if sauce=="True" else "No"
   sauce = "Yes" if sauce else "No"
   print(f"{order}->{size}=>{sauce}")

    
place_order("Burger")
place_order("Fries", size="Large")
place_order("Wrap", "Small", True)

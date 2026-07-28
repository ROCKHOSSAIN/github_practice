def calculate_bill(*dish_prices):
    print("── Order Summary ──")
    for i,price in enumerate(dish_prices,1):
        print(f"Item {i} : ${price}")
    subtotal=sum(dish_prices)
    gst      = round(subtotal * 0.05, 2)   # 5% Tax on food
    total    = round(subtotal + gst, 2)
    print(f"  Subtotal : ¥{subtotal}")
    print(f"  Tax (5%) : ¥{gst}")
    print(f"  TOTAL    : ¥{total}")

calculate_bill(250, 180, 120)

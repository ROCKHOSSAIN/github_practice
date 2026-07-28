
def shipping_cost(*weights_kg):
    total_weight=sum(weights_kg)
    rate=60 if total_weight<=5 else 50
    cost =total_weight * rate
    print(f"Packages    : {len(weights_kg)}")
    print(f"Total weight: {total_weight} kg")
    print(f"Rate        : ¥{rate}/kg")
    print(f"Shipping    : ¥{cost}")
shipping_cost(3.0, 1.5, 2.5, 1.0)   # 4 packages, bulk rate

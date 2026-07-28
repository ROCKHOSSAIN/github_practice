def shipping_cost(*weights_kg):
    total_weight=0
    for weights in weights_kg:
        total_weight+=weights
    rate=60 if total_weight<=5 else 50
    cost=total_weight*rate
    print(total_weight)
    print(rate)
    print(cost)
shipping_cost(1.5, 2.0)            # 2 packages

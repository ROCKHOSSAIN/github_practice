def calculate_bill(*bills):
    sum=0
    for i,prices in enumerate(bills,1):
        sum+=prices
        print(f"{i}:{prices}")
    # gst=(5/100)*sum
    gst=round(sum*0.05,2)
    total_sum=sum+gst
    print(f"Sub total:{sum}")
    print(f"Gst:{gst}")
    print(f"total_sum:{total_sum}")

# Table of 2 — 3 dishes
calculate_bill(250, 180, 120)
def print_daily_special():
    """Print today's featured items for the café board."""
    specials = [
        ("Mango Cold Brew", 180),
        ("Avocado Toast",   220),
        ("Blueberry Muffin",  90),
    ]
    print("\n🌟 TODAY'S SPECIALS 🌟")
    for item, price in specials:
        print(f"  {item:20} ¥{price}")

print_daily_special()
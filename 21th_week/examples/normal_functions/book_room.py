def book_room(guest_name, room_type, **extras):

    print(f"╔══ Booking Confirmation ══╗")
    print(f"  Guest     : {guest_name}")
    print(f"  Room Type : {room_type}")
    if extras:
        for key,value in extras.items():
            print(f"{key.replace("_"," ").title()}:{value}")
    print(f"╚═════════════════════════╝")
    print()
 

book_room(
    "Raj Kapoor", "Suite",
    meal_plan="Full Board",
    sea_view=True,
    early_check_in="10:00 AM",
    spa_package="Couple Massage"
)
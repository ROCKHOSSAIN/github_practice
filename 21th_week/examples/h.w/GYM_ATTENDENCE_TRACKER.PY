# member=[]
# count=0
# def gym_attendance(*members):
#     global count
#     for value in members:
#         member.append(value)
#         count+=1
#     print("Todays Attendence:",count)
#     m="Members"

#     for i,value in enumerate(member):
#         print(f"{value}")


#     if count >= 10:
#         print("Status: Full")
#     else:
#         print("Status: Available")
# # gym_attendance("A","B","C","D",
# #   "E","F","G","H","I","J","K")
# gym_attendance("Riya", "Arjun",
#   "Priya", "Karan")


# 2nd way
def gym_attendance(*members):
    print(f"Today's Attendance: {len(members)}")
    print("Members:",",".join(members))
    if len(members) >= 10:
        print("Status: Full")
    else:
        print("Status: Available")

    print("-" * 30)
gym_attendance("Riya", "Arjun", "Priya", "Karan")

gym_attendance(
    "A", "B", "C", "D",
    "E", "F", "G", "H", "I", "J", "K"
)
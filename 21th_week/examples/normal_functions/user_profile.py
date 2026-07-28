def create_user(username,email,**profile_info):
    user={"username":username,"email":email}
    user.update(profile_info)
    print("new user has been created:")
    for field,value in user.items():
        print(f"  {field:12}: {value}")
    print()

create_user(
    "sunny_k", "sunny@example.com",
    full_name="Sunita Kumar", city="Pune",
    age=27, bio="Python enthusiast 🐍"
)
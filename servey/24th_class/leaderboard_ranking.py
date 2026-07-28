players = [
    {"name": "Zara",  "score": 9800, "level": 12},
    {"name": "Aryan", "score": 9800, "level": 15},
    {"name": "Meera", "score": 7500, "level": 9},
    {"name": "Ravi",  "score": 11200,"level": 18},
    {"name": "Sana",  "score": 6300, "level": 7},
]
ranked=sorted(players,key=lambda p:(-p["score"],p["name"]))
print()

print(ranked)
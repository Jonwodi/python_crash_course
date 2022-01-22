favorite_places = {
    "James": ["Columbia", "Brazil", "France"],
    "Jordan": "Mexico",
    "John": ["USA", "Italy"],
}

print("\n")

for persons, places in favorite_places.items():
    if persons == "James":
        print(f"{persons}' favorite places are {places}")
    elif persons == "Jordan":
        print(f"{persons}' favorite place is {places}")
    else:
        print(f"{persons}'s favorite places are {places}")
    print("\n")

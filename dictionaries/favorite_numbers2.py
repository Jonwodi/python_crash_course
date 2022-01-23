favorite_numbers = {
    "James": [9, 20, 1],
    "Jordan": [8, 35, 100],
    "Sean": [2, 4, 6],
    "Steph": [5, 23, 7],
    "Carlo": [10, 20, 6],
}

print("\n")

for key, value in favorite_numbers.items():
    if key == "James":
        print(f"{key}' favorite number are:")
    else:
        print(f"{key}'s favorite number are:")
    for item in value:
        print(f"{item}")
    print("\n")

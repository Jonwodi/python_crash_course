favorite_numbers = {
    "James": 8,
    "Jordan": 30,
    "Sean": 51,
    "Steph": 31,
    "Carlo": 200,
}

for key, value in favorite_numbers.items():
    if key == "James":
        print(f"{key}' favorite number is {value}.")
    else:
        print(f"{key}'s favorite number is {value}.")

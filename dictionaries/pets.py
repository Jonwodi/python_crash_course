pets = [
    {
        "Kind_of_animal": "Dog",
        "Owner": "Steve",
    },
    {
        "Kind_of_animal": "Cat",
        "Owner": "Stephanie",
    },
    {
        "Kind_of_animal": "Hamster",
        "Owner": "Nicole",
    },
]

rabbit = {
    "Kind_of_animal": "Rabbit",
    "Owner": "Frank",
}


pets.append(rabbit)

for pet in pets:
    print(f'{pet["Owner"]} owns a {pet["Kind_of_animal"]} ')
    for key, value in pet.items():
        print(f"{key}: {value}")
    print("\n")

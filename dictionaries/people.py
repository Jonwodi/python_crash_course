people = [
    {
        "first_name": "Mike",
        "last_name": "Tyson",
        "age": 43,
        "city": "London",
    },
    {
        "first_name": "John",
        "last_name": "Smith",
        "age": 27,
        "city": "Liverpool",
    },
    {
        "first_name": "Steph",
        "last_name": "Day",
        "age": 54,
        "city": "Kent",
    },
]

for person in people:
    name = f'{person["first_name"]} {person["last_name"]}'
    age = f'{person["age"]}'
    city = f'{person["city"]}'
    print(f"{name} is {age} and lives in {city}")

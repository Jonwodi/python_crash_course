cities = {
    "london": {
        "country": "England",
        "fact": "london is the capital of England.",
        "known_as": "LDN",
    },
    "new_york": {
        "country": "USA",
        "fact": "The empire state building is in the new york.",
        "known_as": "Zoo york",
    },
    "las_vegas": {
        "country": "USA",
        "fact": "Las vegas has the best casinos in the world.",
        "known_as": "Sin city",
    },
}


for city, city_info in cities.items():
    print("\n")
    print(f"These are the facts about {city.title()}:")
    for property, property_info in city_info.items():
        print(f"{property}: {property_info}")
    print("\n")

for city, city_info in cities.items():
    country = city_info["country"].title()
    fact = city_info["fact"]
    known_as = city_info["known_as"].title()
    print(f"\n{city.title()} is in {country}.")
    print(f"{fact}.")
    print(f"The city is known as {known_as}.")
print("\n")

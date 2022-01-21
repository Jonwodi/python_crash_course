rivers = {
    "Nile": "Egypt",
    "Mississippi": "United States of America",
    "River thames": "England",
}

print("\n")

# for loop that print dict keys and values
for river, country in rivers.items():
    if river == "River thames":
        print(f"The {river} is in {country}")
    else:
        print(f"The {river} river is in {country}")
print("\n")

# for loop that print dict keys
for river in rivers.keys():
    print(river)
print("\n")

# for loop that print dict values
for country in rivers.values():
    print(country)
print("\n")

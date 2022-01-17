age = 65
person = "Sam"


if age < 2:
    print(f"{person}, is a baby.")
elif age >= 2 and age < 4:
    print(f"{person}, is a toddler.")
elif age >= 4 and age < 13:
    print(f"{person}, is a kid.")
elif age >= 13 and age < 20:
    print(f"{person}, is a teenager.")
elif age >= 20 and age < 65:
    print(f"{person}, is a adult.")
else:
    print(f"{person}, is a elder.")

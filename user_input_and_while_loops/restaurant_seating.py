# Run in the command line terminal to input user data
staff_1 = "james"
staff_2 = "john"

guests_in_dinner_group = input(
    f"{staff_1.title()}, how many people are in the dinner group ?:\n "
)
answer = int(guests_in_dinner_group)

if answer > 8:
    print(
        f"{staff_1.title()}, there is more than 8 people. So they have to wait for a table."
    )
else:
    print(f"{staff_2.title()}, there is {answer} people")
    print(f"Ok {staff_1.title()}, we have a table of {answer} ready for them.")

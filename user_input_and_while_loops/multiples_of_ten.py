# Run in the command line terminal to input user data
header = "IS YOUR NUMBER IN THE 10X TABLE"
print(header + "\n")

user = input("Welcome, what is your name user ?: \n\t")
number = input(f"{user.title()}, what is your number ?: \n\t")

if int(number) % 10 == 0:
    print(
        f"{user.title()}, your number that you selected {int(number)}. Is of multiple of 10."
    )
else:
    print(
        f"{user.title()}, your number that you selected {int(number)}. Is not a multiple of 10."
    )

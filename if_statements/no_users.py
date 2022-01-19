usernames = ["admin", "Jo97", "So96", "Jg96", "Go98"]
del usernames[0:5]

for user in usernames:
    if user == "admin":
        print(f"Hello {user}, would you like to see a status report?")
    else:
        print(f"Hello {user}, thank you for logging in again.")
if usernames == []:
    print("We need to find some users!")

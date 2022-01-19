current_users = ["admin", "jo97", "so96", "jg96", "go98"]
new_users = current_users.copy()
new_users[0:4] = "Jay97", "James96", "Steph90", "JG96"

for user in new_users:
    if user in current_users or isinstance(user, str) and user.upper() == "JG96":
        print(f"You will need to enter a new username. {user} is no longer avaliable.")
    else:
        print(f"This username {user} is avaliable.")

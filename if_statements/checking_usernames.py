current_users = ["admin", "jo97", "so96", "jg96", "go98"]
new_users = current_users.copy()
new_users[0:4] = "Jay97", "James96", "Steph90", "JG96"

for user in new_users:
    if user in current_users or isinstance(user, str) and user.upper() == new_users[3]:
        print(f"You will need to enter a new username. {user} is no longer avaliable.")
    else:
        print(f"This username {user} is avaliable.")
print("\n")


current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry {new_user}, that name is taken.")
    else:
        print(f"Great, {new_user} is still available.")

my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods.copy()
friend_foods[0] = "fish and chips"
friend_foods[2] = "cheesecake"

print("\n")
print("My favourite foods are:")
for food in my_foods:
    print(food)
print("\n")

print("My friend's favourite foods are:")
for food in friend_foods:
    print(food)
print("\n")

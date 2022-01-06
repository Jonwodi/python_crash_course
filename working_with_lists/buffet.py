buffet_food = (
    "pizza",
    "cheeseburger",
    "vegetable fried rice",
    "chicken fried rice",
    "chicken curry",
)

buffet_food_update = list(buffet_food)
buffet_food_update[1] = "chicken kebab"
buffet_food = tuple(buffet_food_update)

print("\n")
for food in buffet_food:
    print(food)
print("\n")

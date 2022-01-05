my_pizzas = ["BBQ Chicken", "Margherita", "Vegan margherita"]
my_pizzas.append("Texas BBQ")

friend_pizzas = my_pizzas.copy()
friend_pizzas[3] = "Chicken feast"

message1 = "My favourite pizzas are:"
message2 = "My friend's favourite pizzas are:"

print("\n")
print(message1)
for pizza in my_pizzas:
    print(pizza)
print("\n")

print(message2)
for pizza in friend_pizzas:
    print(pizza)
print("\n")

print(message1)
my_pizza_list = []
for pizza in my_pizzas:
    pizza = pizza
    my_pizza_list.append(pizza)
print(my_pizza_list)
print("\n")


print(message2)
friend_pizza_list = []
for pizza in friend_pizzas:
    pizza = pizza
    friend_pizza_list.append(pizza)
print(friend_pizza_list)
print("\n")

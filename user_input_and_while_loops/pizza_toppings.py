message = "Hello, what pizza topping would you like ?\n"
message += "\nIf you have finished selecting your pizza toppings."
message += "\nPlease enter 'quit' :\n"

answer = ""
while answer != "quit":
    answer = input(message)
    if answer != "quit":
        print(f"Ok I'll add the {answer} to your pizza.")

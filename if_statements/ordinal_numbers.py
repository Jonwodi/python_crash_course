number_list = list(range(1, 10))
print(number_list)

for number in number_list:
    if number == 1:
        print(f"{str(number) + 'st'}")
    elif number == 2:
        print(f"{str(number) + 'nd'}")
    elif number == 3:
        print(f"{str(number) + 'rd'}")
    else:
        print(f"{str(number) + 'th'}")

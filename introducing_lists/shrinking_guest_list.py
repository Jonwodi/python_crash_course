guests = ["Warren Buffet", "Dan Pena", "Marquett Davon Burton"]

for guest in guests:
    print(f"Hello {guest}, you're invited to dinner\n")
print(f"{guests[2]} can't make dinner anymore\n")

guests[2] = "Michael Jordan"
for guest in guests:
    print(f"Hello {guest}, you're invited to dinner")
    print(f"Dear {guest}, I have found a bigger table for dinner\n")

guests.insert(0, "Ray Lewis")
guests.insert(1, "Khabib Nurmagomedov")
guests.append("Jordan Peterson")

for guest in guests:
    print(f"Hello {guest}, you're invited to dinner\n")
message = "Dear all, I can only invite 2 guests to dinner\n"
print(message)

condition = 1
while condition < 5:
    univited = guests.pop()
    print(
        f"Dear {univited}, I'm very sorry that you're not invited to dinner anymore\n"
    )
    condition += 1

for guest in guests:
    print(f"Dear {guest}, you're still invited to dinner\n")

# guests list is now a empty list
del guests[0:2]
print(guests)


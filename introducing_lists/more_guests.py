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

favorite_languages_poll_taken = {
    "James": "Yes",
    "Jordan": "Yes",
    "Sean": "No",
    "Steph": "No",
    "Carlo": "Yes",
}

favorite_languages_poll_taken["Gaby"] = "No"
favorite_languages_poll_taken["John"] = "Yes"

print("\n")


for person, poll_taken in favorite_languages_poll_taken.items():
    if poll_taken == "Yes":
        print(f"Thank you. {person} for responding and taking the poll.")
    else:
        print(f"Dear {person} you're invited to take the favorite languages poll.")
    print("\n")

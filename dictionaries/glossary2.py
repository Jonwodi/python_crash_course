glossary = {
    "HTML": "HyperText Markup Lanaguage",
    "CSS": "Cascading Style Sheets",
    "Django": "A python web framework",
    "API": "Application Programming Interface",
    "AWS": "Amazon Web Services",
}

glossary["React JS"] = "A Javascript frontend libary/framework"
glossary["AI"] = "Artificial intellegence"
glossary["VS code"] = "Visual studio code"
glossary["Vanilia JS"] = "Plain javascript without using a javascript framework"
glossary["python manage.py runserver"] = "Code used to start Django development server"

tile = "Meanings of programming words:"
print(tile.title())
print("\n")

for key, value in glossary.items():
    print(f"{key}: {value}")
    print("\n")

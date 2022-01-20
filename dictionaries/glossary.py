glossary = {
    "HTML": "HyperText Markup Lanaguage",
    "CSS": "Cascading Style Sheets",
    "Django": "A python web framework",
    "API": "Application Programming Interface",
    "AWS": "Amazon Web Services",
}

tile = "Meanings of programming words:"
print(tile.title())
print("\n")

for key, value in glossary.items():
    print(f"{key}: {value}")
    print("\n")

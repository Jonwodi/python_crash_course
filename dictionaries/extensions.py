favorite_languages = {
    "jen": ["python", "ruby"],
    "sarah": ["c"],
    "edward": ["ruby", "go"],
    "phil": ["python", "haskell"],
}

favorite_languages["john"] = ["java", "javascript"]
favorite_languages["sarah"].append("java")
print("\n")
for name, languages in favorite_languages.items():
    print(f"{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"{language}")
    print("\n")

gcse_subjects = []

gcse_subjects.append("English")
gcse_subjects.append("Chemistry")
gcse_subjects.insert(0, "Maths")
gcse_subjects.insert(3, "Biology")
gcse_subjects[0] = "Physics"
gcse_subjects.pop(1)
del gcse_subjects[0:1]
gcse_subjects.append("History")
gcse_subjects.append("Geography")
gcse_subjects.append("Religious Studies")
gcse_subjects.append("Computer Science")

print("\n")
print(gcse_subjects)

sorted_subjects = sorted(gcse_subjects)
sorted_subjects_reverse = sorted(gcse_subjects, reverse=True)
print(sorted_subjects)
print(sorted_subjects_reverse)

gcse_subjects.reverse()
gcse_subjects.sort()
gcse_subjects.sort(reverse=True)
print(gcse_subjects)
print("\n")

condition = 1
while condition < 3:
    remove = gcse_subjects.pop()
    print(f"This subject {remove}, has been removed from the list\n")
    condition += 1


for subject in gcse_subjects:
    print(f"{subject}, is a GCSE subject")
    message = "These are a few GCSE subjects that you can take in secondary school"
print("\n")
print(message)
subjects_quantity = len(gcse_subjects)
print(f"There are {subjects_quantity} GCSE subjects in this list")
print(f"My favourite GCSE subject is {gcse_subjects[1]}")
print("\n")

ignored_words = input("Enter words to be ignored (separated by commas):\n")
title = input("Enter a title to generate its acronym:\n")
ignored_words = ignored_words.lower().split(", ")
title = title.lower().split()
acronym = ""
for i in title:
    if i not in ignored_words:
        acronym += i[0]
print("The acronym is: " + acronym.upper())
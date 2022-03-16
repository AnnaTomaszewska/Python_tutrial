languages = ["Python", "JavaScrypt", "Ruby"]

language = { language: len(language) for language in languages}
language = { language: len(language) for language in languages if "t" in language}
print(language)

word = "supercalifornistation"

letter_count = { letter: word.count(letter) for letter in word }
print(letter_count)
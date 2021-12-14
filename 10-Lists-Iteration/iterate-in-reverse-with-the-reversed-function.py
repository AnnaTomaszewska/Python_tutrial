#odwracanie listy, od końca do początku za pomocą reverse

the_simpsons = ["Homer", "Marge", "Bart"]

for character in the_simpsons[::-1]: #tak by mozna to zrobić
    print(f"{character} has a total of {len(character)} characters.")

for character in reversed(the_simpsons):
    print(f"{character} has a total of {len(character)} characters.")

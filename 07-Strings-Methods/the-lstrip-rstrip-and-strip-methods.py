#lstrip kasuje początek
#rstrip kasuje końcówkę
#srtip kasuje to co mu się wskaże

empty_space = "     custom    "

print(empty_space.lstrip()) #skasowało początkowe spacje
print(empty_space.rstrip()) #skasowało końcowe spacje
print(empty_space.strip()) #skasowało wszystkie spacje

website = "www.python.org"

print(website.lstrip("w"))
print(website.rstrip("org"))
print(website.strip("worg."))

# Define a fancy_cleanup function that accepts a single string argument
# The function should clean up the whitespace on both sides of the
# argument. It should also replace every occurrence of the letter "g" with the
# letter "z" and every occurence of a space with an exclamation point (!).
#
# fancy_cleanup("       geronimo crikey  ")   => "zeronimo!crikey"
# fancy_cleanup("       nonsense  ")          => "nonsense"
# fancy_cleanup("grade")                      => "zrade"

def fancy_cleanup(text):
    return text.lstrip().rstrip().strip().replace("g", "z").replace(" ", "!")
#mozna tez zamiast wypisywac lstrip i rstrip to samo strip, bo to kasuje wszystko
print(fancy_cleanup("   geronimo crickey   "))


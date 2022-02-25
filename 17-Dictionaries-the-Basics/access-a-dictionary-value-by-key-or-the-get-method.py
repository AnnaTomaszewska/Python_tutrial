# get() Parametry
# get()metoda przyjmuje maksymalnie dwa parametry:

# klucz - klucz do wyszukania w słowniku
# value (opcjonalnie) - Wartość do zwrócenia, jeśliklucznie zostało znalezione. Wartość domyślna to None.

# Zwróć wartość z get()
# get()metoda zwraca:

# wartość dla określonegokluczJeślikluczjest w słowniku.
# Nonejeśliklucznie został znaleziony iwartośćnie jest określony.
# wartośćjeśliklucznie został znaleziony iwartośćjest specyficzne.

gym_membership_package = {
    29: ["Machines"],
    49: ["Machines", "Suplements"],
    70: ["Machines", "Suplements", "Sauna"]
}

print(gym_membership_package[49])
print(gym_membership_package.get(29, ["Basic Dumbbells"])) #zwraca value klucza
print(gym_membership_package.get(100, ["Basic Dumbbells"])) #zwraca Basic Dummbells, bo nie ma klucza 100
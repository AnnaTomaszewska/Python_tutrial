# setdefault() Parametry
# setdefault()przyjmuje maksymalnie dwa parametry:

# klucz - klucz do wyszukania w słowniku
# wartość_domyślna (opcjonalnie) -kluczz wartościądomyślna wartośćjest wstawiany do słownika, jeśli klucza nie ma w słowniku.
# Jeśli nie podano,domyślna wartośćbędzie None.
# Zwracana wartość z setdefault()
# setdefault()zwroty:

# wartośćkluczjeśli jest w słowniku
# Brak, jeśli klucza nie ma w słowniku, a wartość domyślna nie jest określona
# domyślna wartośćJeśliklucznie ma w słowniku idomyślna wartośćjest specyficzne

ice_cream_preferences = {
    "Anna": "Chocolate",
    "Tom": "Vanilla",
    "Kate": "Mango",
    "Bob": "Chocolate"
}

print(ice_cream_preferences.setdefault("Beti", "Chrispy")) #opcja numer 3
print(ice_cream_preferences.setdefault("Beti", "Mango"))
print(ice_cream_preferences.setdefault("Kate", "Vanilla")) #rozpoznało Kate i dopasowało prawdziwa wartosc

# Define a to_dictionary function that accepts a list of strings. 
# The function should return a dictionary where the keys are the strings 
# and the values are their original index positions in the list.
#
# EXAMPLE:
strings = ["Sherlock Holmes", "Hercule Poirot", "Nancy Drew"]
# to_dictionary(detectives) => {'Sherlock Holmes': 0, 'Hercule Poirot': 1, 'Nancy Drew': 2}

def to_dictionary(strings):
    results = {}
    for index, string in enumerate(strings):
        results[string] = index
    return results

print(to_dictionary(strings))

# Define a length_counts function that accepts a list of strings. 
# The function should return a dictionary where the keys represent
# length and the values represent how many strings have that length.
#
# EXAMPLE:
# sa_countries = ["Brazil", "Venezuela", "Argentina", "Ecuador", "Bolivia", "Peru"]
# length_counts(sa_countries) => # {6: 1, 9: 2, 7: 2, 4: 1}
# There is 1 string with 6 letters, 2 strings with 9 letters, 
# 2 strings with 7 letters, and 1 string with 4 letters.

def lenght_counts(elements):
    counts = {}
    for element in elements:
        lenght = len(element)
        current_count = counts.get(lenght, 0) # 0 if the lenght doesn't exist as key
        counts[lenght] = current_count + 1
    return counts

elements = ["Brazil", "Venezuela", "Argentina", "Ecuador", "Bolivia", "Peru"]
print(lenght_counts(elements))
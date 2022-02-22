# Funkcja filter() tworzy nową listę elementów na podstawie wejściowej listy elementów, 
# wybierając tylko te wartości, dla których funkcja testując zwróci prawdę (True).

#można tak:
animals = ["giraffe", "elephant", "dog", "cat", "horse", "cheetah"]
# long_words = [animal for animal in animals if len(animal) > 5]
# print(long_words)

#a z finkcją FILTER tak:

def is_long_animal(animal):
    return len(animal) > 5

print(list(filter(is_long_animal, animals)))
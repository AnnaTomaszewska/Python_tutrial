# Funkcja "map" służy do stosowania funkcji na każdym z elementów listy.

numbers = [1, 4, 6, 7, 9, 11]
# cubes = [number ** 3 for number in numbers]

def cube(number):
    return number ** 3

print(list(map(cube, numbers)))

animals = ["Cat", "Dog", "Lion", "Cheetah"]
print(list(map(len, animals)))
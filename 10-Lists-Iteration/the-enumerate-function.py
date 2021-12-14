errands = ["Go to the gym", "Cooking", "Do a homework"]

print(enumerate(errands))

for idx, errand in enumerate(errands, 1):
    print(f"{errands} is number {idx} on my to do list")

#i to ponumeruje nam czynnosci wg indeksów

# Define an in_list function that accepts a list of strings and a separate string.
# Return the index where the string exists in the list.
# If the string does not exist, return -1.
# Do NOT use the find or index methods.
#
# EXAMPLES
# strings = ["enchanted", "sparks fly", "long live"]
# in_list(strings, "enchanted")  ==> 0
# in_list(strings, "sparks fly") ==> 1
# in_list(strings, "fifteen")    ==> -1
# in_list(strings, "love story") ==> -1

def in_list(strings, words):
    for index, element in enumerate(strings):
        if element == words:
            return index
        else:
            return -1
strings = ["enchanted", "sparks fly", "long live"]
print(in_list(strings, "fifteen"))

# Define a sum_of_values_and_indices function that accepts a list of numbers. 
# It should return the sum of all of the elements along with their index values.
#
# EXAMPLES
# sum_of_values_and_indices([1, 2, 3])    => (1 + 0) + (2 + 1) + (3 + 2) => 9
# sum_of_values_and_indices([0, 0, 0, 0]) => 6
# sum_of_values_and_indices([])           => 0

def sum_of_values_and_indices(numbers):
    total = 0
    for index, number in enumerate(numbers):
        total += index + number
    return total 
print(sum_of_values_and_indices([1, 2, 3]))
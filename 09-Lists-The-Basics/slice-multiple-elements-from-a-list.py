#wybraniekilku elementów z listy

car = ["kierownica", "pedały", "maska", "gaz", "hamulec"]

print(car[2:4]) #pokaże [maska, gaz]
print(car[::2]) #co drugi
print(car[::-1]) #od końca

# Define a split_in_two function that accepts a list and a number.
# If the number is even, return the list elements from the third element to the end of the list.
# If the number is odd, return the list elements from index 0 (inclusive) to 2 (exclusive)
#
# EXAMPLE:
# values = ["a", "b", "c", "d", "e", "f"]
# split_in_two(values, 3)     => ["a", "b"]
# split_in_two(values, 4)     => ["c", "d", "e", "f"]
# split_in_two(values, 1)     => ["a", "b"]
# split_in_two(values, 10)    => ["c", "d", "e", "f"]

#even - parzyste
#odd - nieparzyste

def split_in_two(values, number):
    if number % 2 == 0:
        return values[2:]
    else:
        return values[:2]
values = ["a", "b", "c", "d", "e", "f"]
print(values, 2)

# Declare a nested_extraction function that accepts a list of lists and an index position.
#
# The function should use the index as the basis of finding both the nested list 
# and the element from that list with the given index position
#
# You can assume the number of lists will always be equal to 
# the number of elements within each of them.
#
# nl = [[3, 4, 5], [7, 8, 9], [10, 11, 12]]
# nested_extraction(nl, 0)  => 3
# nested_extraction(nl, 1)  => 8
# nested_extraction(nl, 2)  => 12

def nested_extraction(elements, index):
    return elements[index][index]
nl = [[3, 4, 5], [7, 8, 9], [10, 11, 12]]
print(nested_extraction(nl, 1))


# Declare a beginning_and_end function that accepts a list of elements.
#
# It should return True if the first and last elements in the list are equal and False if they are unequal.
#
# Assume the list will always have at least 1 element.
#
# beginning_and_end([1, 2, 3, 1])     => True
# beginning_and_end([1, 2, 3, 4, 5])  => False
# beginning_and_end(["a", "b", "a"])  => True
# beginning_and_end([15])             => True

def beginning_and_end(elements):
    if elements[0] == elements[-1]:
        return True
    else:
        return False

#albo: return elements[0] == elements[-1]

# Declare a long_word_in_collection function that accepts a list and a string. 
# The function should return True if 
#   - the string exists in the list AND
#   - the string has more than 4 characters.
#
# words = ["cat", "dog", "rhino"]
# long_word_in_collection(words, "rhino")  => True
# long_word_in_collection(words, "cat")    => False
# long_word_in_collection(words, "monkey") => False

def long_word_in_collection(list, arguments):
    if arguments is list and len(arguments) > 4:
        return True
    else:
        return False

#albo: return arguments is list and len(arguments) > 4

#tworzenie nowej listy na podstawie bazowej z użyciem append

powerball_numbers = [3, 6, 12, 15]

def squares(numbers):
    squares = []
    for number in numbers:
        squares.append(number ** 2)
    return squares

print(squares(powerball_numbers))

def even_or_odd(numbers):
    result = []
    for number in numbers:
        if number % 2 ==0:
            result.append(True)
        else:
            result.append(False)
    return result

print(even_or_odd(powerball_numbers))

# Define an only_evens function that accepts a list of numbers. 
# It should return a new list consisting of only the even numbers from the original list.
#
# EXAMPLES
# only_evens([4, 8, 15, 16, 23, 42]) => [4, 8, 16, 42]
# only_evens([1, 3, 5])              => []
# only_evens([])                     => []

def only_evens(numbers):
    result = []
    for number in numbers:
        if number % 2 ==0:
            result.append(number)

    return result

print(only_evens([4, 8, 15, 16, 23, 42]))
print(only_evens([1, 3, 5]))

# Define a long_strings function that accepts a list of strings. 
# It should return a new list consisting of only the strings that have 5 characters or more.
#
# EXAMPLES
# long_strings(["Hello", "Goodbye", "Sam"])  => ["Hello", "Goodbye"]
# long_strings(["Ace", "Cat", "Job"])        => []
# long_strings([])                           => []

def long_strings(strings):
    result = []
    for string in strings:
        if len(string) >= 5:
            result.append(string)
    return result
print(long_strings(["Hello", "Goodbye", "Sam"]))
print(long_strings(["Ace", "Cat", "Job"]))

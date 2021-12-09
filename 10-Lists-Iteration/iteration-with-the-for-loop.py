numbers = [1, 3, 5, 6, 10]

for number in numbers:
    print(number * number)

pisarze = ["Kochanowski", "Sienkieiwcz", "Mickiewicz", "Python"]
for pisarz in pisarze:
    print(len(pisarze))

print(pisarz)
print(number)

# Define a sum_of_lengths function that accepts a list of strings.
# The function should return the sum of the string lengths.
#
# EXAMPLES
# sum_of_lengths(["Hello", "Bob"])                  => 8
# sum_of_lengths(["Nonsense"])                      => 8
# sum_of_lengths(["Nonsense", "or", "confidence"])  => 20

def sum_of_lengths(strings):
    total = 0
    for string in strings:
        total += len(string)
    return total

# Define a product function that accepts a list of numbers.
# The function should return the product of the numbers.
# The list will always have at least one value
#
# EXAMPLES
# product([1, 2, 3])     => 6
# product([4, 5, 6, 7])  => 840
# product([10])          => 10

def product(numbers):
    total = 1
    for number in numbers:
        total *= number
    return total

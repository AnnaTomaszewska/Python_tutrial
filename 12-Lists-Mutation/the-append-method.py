#append dodaje kolejną wartość do listy

countries = ["China", "Poland", "Germany"]
print(countries)
print(len(countries))

countries.append("France")
print(countries)
print(len(countries))

# Declare a length_match function that accepts a list of strings and an integer.
# It should return a count of the number of strings whose length is equal to the number.
#
# EXAMPLES
# length_match(["cat", "dog", "kangaroo", "mouse"], 3))  => 2
# length_match(["cat", "dog", "kangaroo", "mouse"], 5))  => 1
# length_match(["cat", "dog", "kangaroo", "mouse"], 4))  => 0
# length_match([], 5))                                   => 0

def length_match(strings, integer):
    count = 0
    for string in strings:
        if len(string) == integer:
            count += 1
        return count
           
length_match(["cat", "dog", "kangaroo", "mouse"], 3)
print(length_match)

# Declare a sum_from function that accepts two numbers as arguments.
# The second number will always be greater than the first number.
# The function should return the sum of all numbers from the first number to the second number (inclusive).
#
# EXAMPLES
# sum_from(1, 2)   # 1 + 2                  => 3
# sum_from(1, 5)   # 1 + 2 + 3 + 4 + 5      => 15
# sum_from(3, 8)   # 3 + 4 + 5 + 6 + 7 + 8  => 33
# sum_from(9, 12)  # 9 + 10 + 11 + 12       => 42

def sum_from(numbers, values):
    total = 0
    for number in range(numbers, values + 1): #=1 po to, aby ostatnia cyfra była wliczona 
         total += number
    return total

print(sum_from(1, 2))

# Declare a same_index_values function that accepts two lists.
# The function should return a list of the index positions in which the two lists have equal elements
#
# EXAMPLES
# same_index_values([1, 2, 3], [3, 2, 1])                         => [1]
# same_index_values(["a", "b", "c", "d"], ["c", "b", "a", "d"])   => [1, 3]

def same_index_values(list1, list2):
    results = []
    for index, number in enumerate(list1):
        if number == list2[index]:
            results.append(index)
    return results

print(same_index_values([1, 2, 3], [3, 2, 1]))
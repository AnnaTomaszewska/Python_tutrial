#funckan SUM sumuje wartosci

print(sum([5, 7, 1, 9]))

# Declare a greater_sum function that accepts two lists of numbers.
# It should return the list with the greatest sum.
# You can assume the lists will always have different sums.
#
# EXAMPLES
# greater_sum([1, 2, 3], [1, 2, 4]) => [1, 2, 4]
# greater_sum([4, 5], [2, 3, 6])    => [2, 3, 6]
# greater_sum([1], [])              => [1]

def greater_sum(lists1, lists2):
    if sum(lists1) > sum(lists2):
        return lists1
    else:
        return lists2

print(greater_sum([1, 2, 3], [1, 2, 4]))

# Declare a sum_difference function that accepts two lists of numbers.
# It should return the difference between the sum of values in the first list and the second list
#
# EXAMPLES
# sum_difference([1, 2, 3], [1, 2, 4]) => 6 - 7 => -1
# sum_difference([4, 5], [2, 3, 6])    => 9 - 11 => -2
# sum_difference([1], [])              => 1

def sum_difference(l1, l2):
    return sum(l1) - sum(l2)

print(sum_difference([4, 5], [2, 3, 6]))
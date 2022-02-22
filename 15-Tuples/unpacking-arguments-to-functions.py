from ast import arg


employee = ("Bob", "Johnson", "Junior", "26")

first_name, last_name, *details = employee
print(first_name)
print(last_name)
print(details)

# Given the tuple below, destructure the three values and
# assign them to position, city and salary variables
# Do NOT use index positions (i.e. job_opening[1])
job_opening = ("Software Engineer", "New York City", 100000)

position, city, salary_variables = job_opening
print(position, city, salary_variables)


# Given the tuple below, 
# - destructure the first value and assign it to a street variable
# - destructure the last value and assign it to a zip_code variable
# - destructure the middle two values into a list and assign it to a city_and_state variable
address = ("35 Elm Street", "San Francisco", "CA", "94107")

street, *city_and_state, zip_code = address
print(street)
print(city_and_state)
print(zip_code)

# Declare a sum_of_evens_and_odds function that accepts a tuple of numbers.
# It should return a tuple with two numeric values:
# -- the sum of the even numbers
# -- the sum of the odd numbers.
#
# sum_of_evens_and_odds((1, 2, 3, 4))   => (6, 4)
# sum_of_evens_and_odds((1, 3, 5))      => (0, 9)
# sum_of_evens_and_odds((2, 4, 6))      => (12, 0)

def sum_of_evens_and_odds(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    odd_numbers = [num for num in numbers if num % 2 != 0]
    
    return(sum(even_numbers), sum(odd_numbers))

print(sum_of_evens_and_odds((1, 2, 3, 4)))


def accept_stuff(*args):
    print(args)

accept_stuff(1, 2)

def my_max(*numbers):
    greatest = numbers[0]
    for number in numbers:
        if number > greatest:
            greatest = number
    return greatest

print(my_max(6, 5, 8, 3))

def products(a, b):
    return a * b

numbers = [3, 5] #lista
numbers = (3, 5) #tuples

print(products(*numbers)) # dzięki "*" możemy traktować elementy a i b jako jedno,
# bez tego "numbers" byłoby wartością "a"


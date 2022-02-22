# Declare a months tuple with the last 4 months of the year (September, October, November, December) as strings.
# Make sure the first letter of each month is capitalized.

months = ("September", "October", "November", "December") #to nie lista, to tuple 

print(tuple(["September", "October", "November", "December"]))
print(tuple(months))

# Create a faves variable with a list of your 3 three favorite movies as strings. 
# Use the tuple function to convert the list to a tuple and save the result in a movies variable.

movies = ["How I met your mother", "Friends", "The bold type"]
#faves = tuple(movies)
print(tuple(movies))

# Create a numbers_a, numbers_b, and numbers_c tuple. 
# Each tuple should contain 3 integers. 
# Declare an all_numbers tuple containing these three tuples.

numbers_a = (2, 5, 8)
numbers_b = (1, 4, 7)
numbers_c = (3, 6, 9)

all_numbers = (numbers_a, numbers_b, numbers_c)

print(all_numbers)


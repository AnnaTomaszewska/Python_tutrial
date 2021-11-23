def add(a, b):
    return a + b
    print(a + b)


result = add(5, 7)
print(result)

# Define a easy_money function that accepts no parameters 
# and always returns the value 100.
def easy_money():
    print(100) #źle
    return 100 #dobrze - dzięki return ta wartość zawsze będzie zwracana

easy_money()

# Define a best_food_ever function that accepts 
# no parameters and always returns the string “Sushi”.
def best_food_ever():
    print("Sushi") #źle
    return "Sushi" #dobrze

best_food_ever()

# Define a convert_to_currency function that accepts a single parameter (an integer). 
# The function should convert the argument to a string, prefix it with a dollar sign, and return the result.
# 
# EXAMPLES:
# convert_to_currency(15)    => "$15"
# convert_to_currency(8)     => "$8"

def convert_to_currency(an_integer):
    return an_integer
    print(str(an_integer))

result = convert_to_currency(15)
print("$", result) #można lepiej patrz poniżej

def convert_to_currency(amount):
    return "$" + str(amount)

# Define a string_adder function that accepts two strings (a and b) as arguments.
# It should return a concatenated version of the arguments with a space in between.
# If the user does not pass in arguments, both arguments should default to an empty string.
#
# EXAMPLES
# string_adder("Hello", "World")      => "Hello World"
# string_adder("Emilio", "Estevez")   => "Emilio Estevez"
# string_adder()                      => " "
# string_adder("Tiger")               => "Tiger "

def string_adder(a = "", b = ""):
    return a + " " + b

print(string_adder("hello", "world"))
print(string_adder("tiger"))
print(string_adder())

# Define a multiplier function that accepts three integers as arguments.
# Return the product of the arguments. The product is the total when values are multiplied together.
# If the user does not provide any arguments, all three parameters should have default arguments of 1.
#
# EXAMPLES
# multiplier(2, 2, 2)    => 8
# multiplier()           => 1
# multiplier(3)          => 3
# multiplier(2, 5)       => 10

def multiplier(a = 1, b = 1, c = 1):
    return a * b * c 

print(multiplier(2, 2, 2)) #multiplier = mnożnik
print(multiplier())
print(multiplier(7))

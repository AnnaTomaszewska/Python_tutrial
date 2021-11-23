def positive_or_negative(number):
    if number > 0:
        return "Positive!"
    elif number < 0:
        return "Negative"
    else:
        return "It's zero!"

print(positive_or_negative(6))
print(positive_or_negative(-4))
print(positive_or_negative(0))

#moze byc tak jak ponizej, ale to wyzej z "elif"
#jest też super sposobem

def positive_or_negative(number):
    if number > 0:
        return "Positive!"
    if number < 0:
        return "Negative"
    else:
        return "It's zero!"

print(positive_or_negative(6))
print(positive_or_negative(-4))
print(positive_or_negative(0))

def calculator(operation, a, b):
    if operation == "add":
        return a + b
    elif operation == "odejmowanie":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        return a / b 
    else:
        return "I don't know" 

print(calculator("add", 4, 7))
print(calculator("odejmowanie", 4, 7))
print(calculator("multiply", 4, 7))
print(calculator("divide", 4, 7))
print(calculator("translator", 4, 7))

# Declare a negative_energy function that accepts a numeric argument and returns its absolute value. 
# The absolute value is the number's distance from zero.
# 
# negative_energy(5)    => 5
# negative_energy(10)   => 10
# negative_energy(-5)   => 5
# negative_energy(-8)   => 8
# negative_energy(0)    => 0

def negative_energy(number):
    if number > 0: #or number >= 0
        return number
    elif number < 0:
        return -number #or -1 * number
    else:
        return 0 #jesli number >= 0 to tutaj return number

print(negative_energy(5))
print(negative_energy(-5))
print(negative_energy(0))

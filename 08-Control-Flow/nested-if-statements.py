skladnik1 = "Pizza"
skladnik2 = "Schabowy"

if skladnik1 == "Pizza":
    if skladnik2 == "Schabowy":
        print("Pizza i Schabowy to super połącznie")
    else:
        print("Zjedzmy samą Pizze")
else:
    print("Nie mam pomysłu")

skladnik1 = "Pizza"
skladnik2 = "Makaron"

if skladnik1 == "Pizza":
    if skladnik2 == "Schabowy":
        print("Pizza i Schabowy to super połącznie")
    else:
        print("Zjedzmy samą Pizze")
else:
    print("Nie mam pomysłu")

skladnik1 = "Schabowy"
skladnik2 = "Makaron"

if skladnik1 == "Pizza":
    if skladnik2 == "Schabowy":
        print("Pizza i Schabowy to super połącznie")
    else:
        print("Zjedzmy samą Pizze")
else:
    print("Nie mam pomysłu")

#to samo mozemy zapisać inaczej:

if skladnik1 == "Pizza" and skladnik2 == "Schabowy":
    print("Pizza i Schabowy to super połącznie")
elif skladnik1 == "Pizza":
    print("Zjedzmy samą Pizze")
else:
    print("Nie mam pomysłu")

# Define a divisible_by_three_and_four function that accepts a number as its argument. 
# It should return True if the number is evenly divisible by both 3 and 4 . 
# It should return False otherwise.
#
# divisible_by_three_and_four(3)   => False
# divisible_by_three_and_four(4)   => False
# divisible_by_three_and_four(12)  => True
# divisible_by_three_and_four(18)  => False
# divisible_by_three_and_four(24)  => True

def divisible_by_three_and_four(number):
    return number % 3 == 0 and number % 4 == 0

print(divisible_by_three_and_four(12))
print(divisible_by_three_and_four(15))


# Declare a string_theory function that accepts a string as an argument. 
# It should return True if the string has more than 3 characters 
# and starts with a capital “S”. It should return False otherwise.
#
# string_theory("Sansa") => True
# string_theory("Story") => True
# string_theory("See") => False
# string_theory("Fable") => False

def string_theory(word):
    return len(word) > 3 and word.startswith("S")
#albo: return len(word) > 3 and word[0] == "S"

print(string_theory("Sansa"))
print(string_theory("Fable")) 
    
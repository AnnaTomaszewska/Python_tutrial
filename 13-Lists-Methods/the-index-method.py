#pokazuje, na której pozycji dane wyrażenie jest w liście

pizzas = [
    "Salami",
    "Pepperoni",
    "Sausage",
    "Mozzarella",
    "Pepperoni"
]

print(pizzas.index("Pepperoni")) #zawsze pokazuje pierwszy index

#możemy też zaczaczyć, od ktrego ma zaczynać ale ten wskazany jest wykluczany

print(pizzas.index("Pepperoni", 3))

# Define an encrypt_message function that accepts a string.
# The input string will consist of only alphabetic characters.
# The function should return a string where all characters have been moved
# "up" two spots in the alphabet. For example, "a" will become "c".
#
# EXAMPLES
# encrypt_message("abc") => "cde"
# encrypt_message("xyz") => "zab"
# encrypt_message("")    => ""

#DO ROZWIĄZANIA!!!

#modulo 17 % 12 --> 5
    # 17 / 12 = 1
    # 1 * 12 = 12
    # 17 - 12 = 5

def encrypt_message(message):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encrypted = ""
    for letter in message:
        encrypted_letter_index_position = (alphabet.index(letter) + 2) % 26 
        encrypted += encrypted_letter_index_position

    return encrypted


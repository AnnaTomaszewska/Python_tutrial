word = "queueing"

print(word.count("u"))
#liczy ile razy występuje dany znak

print(word.count("ue"))
print(word.count("u") + word.count("e"))

# Define a vowel_count function that accepts a string argument.
# The function should return the count of vowels in the string.
# The 5 vowels are "a", "e", "i", "o", and "u".
# You can assume the string will be in all lowercase.
#
# EXAMPLES:
# vowel_count("estate")        => 3
# vowel_count("helicopter")    => 4
# vowel_count("ssh")           => 0

def vowel_count(word):
    return word.count("a" + "e" + "i" + "o" + "u") #źle
    return word.count("a") + word.count("e") + word.count("i") + word.count("o") + word.count("u")

vowel_count("helicopter")
vowel_count("ssh")

# Define a find_my_letter function that accepts two arguments: a string and a character
# The function should return the first index position of the character in the string
# The function should return a -1 if the character does not exist in the string
#
# EXAMPLES:
# find_my_letter("dangerous", "a")    => 1
# find_my_letter("bazooka", "z")      => 2
# find_my_letter("lollipop", "z")     => -1

def find_my_letter(word, str):
    return word.find(str)

find_my_letter("dangerous", "a")
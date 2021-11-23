print(len("Ania")) #len pokazuje ile jest znaków (nie działa na cyfry)
print(len("Najlepsza"))
print(len(" "))
print(len(""))
print(len("$%^&*"))

print("Ania" + "Tomaszewska")
print("Ania" + " " + "Tomaszewska")
print("Ania " + "Tomaszewska")
print("Ania" + " Tomaszewska")

print("a" "b" "c")
print("&&" * 5)

# Define a long_word function that accepts a string. 
# The function should return a Boolean that reflects whether the string has more than 7 characters.
# 
# EXAMPLES:
# long_word("Python")         => False
# long_word("magnificent")    => True
def long_word(word):
    return len(word) > 7 
    
print(long_word("niesamowity"))


# Define a first_longer_than_second function that accepts two string arguments. 
# The function should return a True if the first string is longer than the second 
# and False otherwise (including if they are equal in length).
#
# EXAMPLES:
# first_longer_than_second("Python", "Ruby")     => True
# first_longer_than_second("cat", "mouse")       => False
# first_longer_than_second("Steven", "Seagal")   => False

def first_longer_than_second(a, b):
    return len(a) > len(b)

print(first_longer_than_second("mama", "babcia"))

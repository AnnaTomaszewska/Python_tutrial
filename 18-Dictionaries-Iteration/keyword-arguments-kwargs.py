def collect_keywords_arguments(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(f"The kye is {key} and the value is {value}")

collect_keywords_arguments(a = 2, b = 4, c = 6)

def args_and_kwargs(a, b, *args, **kwargs):
    print(args) # wypisze 4, 5, 6, ponieważ 2 i 3 są jako a i b


args_and_kwargs(2, 3, 4, 5, 6)

# Declare a plenty_of_arguments function that accepts two parameters (a and b)
# and an additional **kwargs parameter.
#
# The function should return True if the sum of a, b, and the values of 
# **kwargs is greater than 100. It should return False otherwise.
#
# EXAMPLES:
# plenty_of_arguments(20, 30)                          => False
# plenty_of_arguments(a = 50, b = 75)                  => True
# plenty_of_arguments(a = 50, b = 25, c = 50)          => True
# plenty_of_arguments(a = 25, b = 25, c = 25, d = 25)  => False
# plenty_of_arguments(a = 25, b = 25, c = 25, d = 26)  => True

def plenty_of_arguments(a, b, **kwargs):
        return a + b + sum(kwargs.values()) > 100 

print(plenty_of_arguments(20, 30))
# Python list pop() is an inbuilt function in Python that removes and returns the last value from the 
# List or the given index value\

release_dates = {
    "Python": 1991,
    "Ruby": 1995,
    "Java": 1995,
    "Go": 2007
}

release_dates.pop("Java")
print(release_dates) #skasowało "Java"

# Declare a delete_keys function that accepts two arguments:
# a dictionary and a list of strings. 
# For each string in the list, if the string exists as a dictionary key, 
# delete the key-value pair from the dictionary. 
#
# If the string does not exist as a dictionary key, avoid an error. 
# The return value should be the modified dictionary object.
#
# EXAMPLE:
# my_dict = {
#   "A": 1,
#   "B": 2,
#   "C": 3
# }
#
# strings = ["A", "C"]
# delete_keys(my_dict, strings) => {'B': 2}

my_dict = {
    "A": 1,
    "B": 2,
    "C": 3
}

def delete_function(my_dict, strings):
    for string in strings:
        if string in my_dict:
            my_dict.pop(string)
    return my_dict

print(delete_function)
    



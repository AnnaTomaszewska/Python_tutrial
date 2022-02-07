print(["abcdefghijklmnopqrstuvwxyz".index(char) for char in "donut"])
print([number / 2 for number in range(20)])

donuts = [
    "Vanilla Cream",
    "Jelly",
    "Chocolate Cream", 
    "Glazed", 
    "Boston Cream"
]

# creamy_donuts = []
# for donut in donuts:
#     if "Cream" in donut:
#         creamy_donuts.append(donut)
# print(creamy_donuts)

creamy_donuts = [donut for donut in donuts if "Cream" in donut]
print(creamy_donuts)

# Uncomment the commented lines of code below and complete the list comprehension logic

# The floats variable should store the floating point values 
# for each string in the values list.
values = ["3.14", "9.99", "567.324", "5.678"]
floats = [float(value) for value in values]

# The letters variable should store a list of 5 strings. 
# Each of the strings should be a character from name concatenated together 3 times.
# i.e. ['BBB', 'ooo', 'rrr', 'iii', 'sss']
name = "Boris"
letters = [char * 3 for char in name]

# The 'lengths' list should store a list with the lengths
# of each string in the 'elements' list
elements = ["Hydrogen", "Helium", "Lithium", "Boron", "Carbon"]
lengths = [len(element) for element in elements]

# Declare a destroy_elements function that accepts two lists.
# It should return a list of all elements from the first list that are NOT contained in the second list.
# Use list comprehension in your solution.
#
# EXAMPLES
# destroy_elements([1, 2, 3], [1, 2])      => [3]
# destroy_elements([1, 2, 3], [1, 2, 3])   => []
# destroy_elements([1, 2, 3], [4, 5])      => [1, 2, 3]

def destroy_elements(first, second):
    return [element for element in first if element not in second]
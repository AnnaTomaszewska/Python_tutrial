bubble_tea_flavors = [
    ["Mango", "Banana", "Peach"],
    ["Honey", "Strawberry"],
    ["Lime"]
]

print(bubble_tea_flavors[0])
print(bubble_tea_flavors[0][1])

all_flavors = []

for flavors_pack in bubble_tea_flavors:
    for flavor in flavors_pack:
        all_flavors.append(flavor)

print(all_flavors)

# Define a nested_sum function that accepts a list of lists of numbers
# The function should return the sum of the values
# The list may contain empty lists
#
# EXAMPLES
# nested_sum([[1, 2, 3], [4, 5]])            => 15
# nested_sum([[1, 2, 3], [], [], [4], [5]])  => 15
# nested_sum([[]])                           => 0

def nested_sum(lists):
    total = 0
    for list in lists:
        for number in list:
            total += number
    return total 
    
print(nested_sum([[1, 2, 3], [4, 5]]))

# Define a fancy_concatenate function that accepts a list of lists of strings
# The function should return a concatenated string
# The strings in a list should only be concatenated if the length of the list is 3
#
# EXAMPLES
# fancy_concatenate([["A", "B", "C"]])                        => "ABC"
# fancy_concatenate([["A", "B", "C"], ["D", "E", "F"]])       => "ABCDEF"
# fancy_concatenate([["A", "B", "C"], ["D", "E", "F", "G"]])  => "ABC"
# fancy_concatenate([["A", "B", "C"], ["D", "E"]])            => "ABC"
# fancy_concatenate([["A", "B"], ["C", "D"]])                 => ""

def fancy_concatenate(lists):
    total = ""
    for list in lists:
            if len(list) == 3:
                for string in list:
                    total += string
             
    return total 
print(fancy_concatenate([["A", "B", "C"]]))
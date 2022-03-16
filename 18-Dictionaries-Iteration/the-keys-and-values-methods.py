cryptocurrency_price = {
    "Bitcoin": 40000,
    "Ethereum": 1500,
    "Litecoin": 400
}

print(cryptocurrency_price.keys()) #pokazuje klucze
print(cryptocurrency_price.values()) #pokazuje wartości

for currency in cryptocurrency_price.keys():
    print(f"The next currency is {currency}")


# Declare a common_elements function that accepts a dictionary
# It should return a list with all of the elements that are found
# as both a key and a value in the dictionary
#
# HINT: Use the in operation to check for inclusion in a view or list object
#
# EXAMPLE:
# my_dict = {
#   "A": "K",
#   "B": "D",
#   "C": "A",
#   "D": "Z"
# }
#
# common_elements(my_dict) => ["A", "D"]

def common_elements(dict):
    return [key for key in dict.keys() if key in dict.values()]

dict = {
  "A": "K",
  "B": "D",
  "C": "A",
  "D": "Z"
}

print(common_elements(dict))
    
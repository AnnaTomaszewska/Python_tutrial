numbers = [4, 7, 2, 9]
print(sorted(numbers))

cryptocurrency_price = {
    "Litecoin": 400,
    "Bitcoin": 40000,
    "Ethereum": 1500
}

print(sorted(cryptocurrency_price))

for key, values in sorted(cryptocurrency_price.items()): #sortuje klucze np alfabetycznie
    print(f"The next crypto is a {key} with price {values}") 
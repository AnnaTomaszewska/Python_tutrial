concert_attendees = [
    {"name": "Taylor", "section": 400, "price paid": 99.99},
    {"name": "Beti", "section": 200, "price paid": 149.99},
    {"name": "Kate", "section": 100, "price paid": 0.00}
]

for attendee in concert_attendees:
    for key, value in attendee.items():
        print(f"The {key} is {value}.")

# Assign a list of four dictionaries to a "complexity" variable below

# The first and third dictionaries should have two key-value pairs
# For those dictionaries, the keys should be strings and the values should be Booleans

# The second and fourth dictionaries should have three key-value pairs
# For those dictionaries, the keys shoulds be floats and the values should be list of strings. 
# The lists can be of any length.

complexity = [
    {"A": True, "B": False},
    {25.00: ["Skirt", "Jeans"], 3.6: ["Apples", "Wine"]},
    {"C": True, "D": False},
    {199.98: ["concert", "trip"]}
]
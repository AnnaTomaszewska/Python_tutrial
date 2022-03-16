capitals = {
    "New York": "Albany", 
    "California": "Sacramento",
    "Texas": "Austin"
}

invert = { capital: state for state, capital in capitals.items()}
print(invert)

invert = { capital: state for state, capital in capitals.items() if len(state) != len(capital)}
print(invert)

# You are writing a Python program to model a remote control
# for a television set. Declare a stations_to_numbers
# function that accepts a dictionary. The keys will be
# channel numbers and the values will be the station names.
# For example...
# channels = {
#   2: "CBS",
#   4: "NBC",
#   5: "FOX",
#   7: "ABC"
# }
# The stations_to_numbers function should return an
# inverted dictionary where the keys are the station names
# and the values are the channel numbers
#
# stations_to_numbers(channels) => {'CBS': 2, 'NBC': 4, 'FOX': 5, 'ABC': 7}

channels = {
  2: "CBS",
  4: "NBC",
  5: "FOX",
  7: "ABC"
}

stations_to_numbers = { value: key for key, value in channels.items()}
print(stations_to_numbers)

def stations_to_numbers(channels):
    return { value: key for key, value in channels.items()}

print(channels)

# Declare a coaster_conversion function that accepts a dictionary
# The keys of the dictionary will be strings representing roller coasters
# The values will be the heights of each coaster in meters
#
# Return a new dictionary with the same keys.
# The values should be the heights converted from meters to feet,
# The final values (in feet) should also be rounded to the closest integer
# HINT: 1 meter is equal to 3.28084 feet
# HINT: The round function rounds a number to the nearest integer
#
# coasters = {
#   "Kingda Ka": 139,
#   "Top Thrill Dragster": 130,
#   "Superman: Escape From Krypton": 126
# }
#
# coaster_conversion(coasters) => {'Kingda Ka': 456, 'Top Thrill Dragster': 426, 'Superman: Escape From Krypton': 413}

coasters = {
  "Kingda Ka": 139,
  "Top Thrill Dragster": 130,
  "Superman: Escape From Krypton": 126
}

def coaster_conversion(coasters):
    
    return { coaster: round(meters * 3.28084) for coaster, meters in coasters.items()}

print(coaster_conversion(coasters))

    
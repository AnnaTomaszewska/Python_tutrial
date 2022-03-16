def height_to_meters(feet, inches):
    total_inches = (feet * 12) + inches
    return total_inches * 0.0234

print(height_to_meters(5, 11))

stats = {
    "feet": 5,
    "inches": 11
}

print(height_to_meters(**stats))
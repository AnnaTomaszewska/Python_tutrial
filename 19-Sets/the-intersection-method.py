candy_bars = {"Mars", "Snickers", "Milkey Way"}
sweet_things = {"Chocoalte", "Mars", "100 Grand"}

print(candy_bars.intersection(sweet_things))
print(candy_bars & sweet_things)

value = {3.0, 4.0, 5.0}
more_value = {3, 4, 5, 6}

print(value.intersection(more_value))
print(more_value.intersection(value))
print(value & more_value)
print(more_value & value)
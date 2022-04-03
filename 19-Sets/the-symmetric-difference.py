candy_bars = {"Mars", "Snickers", "Milkey Way"}
sweet_things = {"Chocoalte", "Mars", "100 Grand"}

print(candy_bars.symmetric_difference(sweet_things))
print(candy_bars ^ sweet_things)

print(sweet_things.symmetric_difference(candy_bars))
print(sweet_things ^ candy_bars)

# symmetric.difference pokazuje wszystkie elementy, które nie są wspólne ze wszystkich zestawów 
from wsgiref.simple_server import software_version


candy_bars = {"Mars", "Snickers", "Milkey Way"}
sweet_things = {"Chocoalte", "Mars", "100 Grand"}

print(candy_bars.union(sweet_things))
print(sweet_things.union(candy_bars))

print(candy_bars | sweet_things)
print(sweet_things | candy_bars)

#union łączy zestawy
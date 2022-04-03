# Frozen set to po prostu niezmienna wersja obiektu zestawu Pythona . 
# Chociaż elementy zestawu można modyfikować w dowolnym momencie, elementy zamrożonego 
# zestawu pozostają takie same po utworzeniu.

mr_freeze = frozenset([1, 2, 3, 2])
print(mr_freeze) # zwróci bez powtórek

print({ mr_freeze: "Some value" })
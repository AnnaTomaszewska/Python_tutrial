# Możemy dodać pojedynczy element za pomocą add()metody i wiele elementów 
# za pomocą update()metody. Metoda update()może przyjąć jako swój argument 
# krotki , listy, ciągi znaków lub inne zestawy. We wszystkich przypadkach unika się duplikatów.

my_friends = {
    "Kate",
    "Bet",
    "Malgo"
}

my_friends.add("Sylwia")
print(my_friends) # doda wlosowe miejsce

my_friends.update(("Tom", "Kinga")) 
print(my_friends)
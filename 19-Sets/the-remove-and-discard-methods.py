# Poszczególny przedmiot można usunąć z zestawu za pomocą metod discard()i remove().
# Jedyna różnica między nimi polega na tym, że discard()funkcja pozostawia zestaw niezmieniony, 
# jeśli element nie jest obecny w zestawie. Z drugiej strony remove()funkcja zgłosi błąd w takim stanie 
# (jeśli element nie występuje w zestawie).

my_friends = {"Tom", "Kate", "Beti", "Malgo"}
my_friends.remove("Tom")
print(my_friends)

my_friends.discard("Anna")
print(my_friends)
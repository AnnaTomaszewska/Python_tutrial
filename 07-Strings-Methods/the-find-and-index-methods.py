funkcja = "Anna Tomaszewska"

print(funkcja.find("n"))
#wskazuje, na której pozycji jest dany znak
print(funkcja.find("a", 4))

print(funkcja.index("T"))
#działatak samo jak find, tylko, że jak nie będzie
#jakiegos znaku to wyrzuci błąd, a w "find" -1
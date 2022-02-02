#usuwa pierwszy element jeśli jest powielony
#jeśli jest jeden taki to też usuwa
#jeśli niema takiego to wyrzuca value error

names = ["Anna", "Thomas", "Kate", "Thomas"]
names.remove("Thomas")
print(names)
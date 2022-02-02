#list.extend(iterable)
#Rozszerza listę przez dodanie wszystkich elementów iterable’a.

names = ["Anna", "Thomas", "Kate"]
names.extend(["Monica", "Beti"])

print(names)

#można też tak:

names = ["Anna", "Thomas", "Kate"]
different_names = ["Monica", "Beti"]

names += different_names

print(names)
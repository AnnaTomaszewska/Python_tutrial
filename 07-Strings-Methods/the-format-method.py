#name, przymiotnik, rzeczownik

mad_libs = "{} śmieje się z {} {}."

#print(mad_libs.format("Anna", "zabawnego", "chomika"))
#format dodaje to co powinno byc w {}

#mad_libs = "{0} śmieje się z {1} {2}."
#print(mad_libs.format("Anna", "zabawnego", "chomika"))

#mad_libs = "{name} śmieje się z {przymiotnik} {rzeczownik}."
#print(mad_libs.format(name = "Anna", przymiotnik = "zabawnego", rzeczownik = "chomika"))

mad_libs = "{name} śmieje się z {przymiotnik} {rzeczownik}."

name = input("Podaj imię: ")
przymiotnik = input("Podaj przymiotnik: ")
rzeczownik = input("Podaj rzeczownik: ")

print(mad_libs.format(name = name, przymiotnik = przymiotnik, rzeczownik = rzeczownik))
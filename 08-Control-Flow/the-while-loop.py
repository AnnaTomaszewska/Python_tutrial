#count = 0
#
#while count <= 5:
#    print(count)
#    count += 1
#
#print(count)

invalid_number = True

while  invalid_number:
    user_value = int(input("Wpisz liczbę większą od 10: "))
    if user_value > 10:
        print(f"Super robota! {user_value} to świetny wybór")
        invalid_number = False #tego nie czaje
    else:
        print("Spróbuj jeszcze raz")

#jeśli ktoś nie zastosuje się to wymagań
#wpisze liczbę mniejszą od 10 to polecenie wywoła się jeszcze raz

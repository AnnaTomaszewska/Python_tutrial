#continue - jeśli napotka "przeszkodę" polecenie ma isc dalej

def sum_of_positive_numbers(values):
    total = 0
    for value in values:
        if value < 0:
            continue
       
        total += value
        
    return total #zawsze musi byc "tab"wczesniej niz polecenie

print(sum_of_positive_numbers([1, 2, -3, 6])) 




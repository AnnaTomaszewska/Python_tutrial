#Funkcja zip łączy ze sobą elementy z różnych obiektów iterowalnych, takich jak listy, krotki, zbiory, i zwraca nam iterator. Możemy jej użyć to połączenia ze sobą dwóch list:


#id = [1, 2, 3, 4]
#leaders = ['Elon Mask', 'Tim Cook', 'Bill Gates', 'Yang Zhou']
#record = zip(id, leaders)

#print(record)
# <zip object at 0x7f266a707d80>

#print(list(record))
# [(1, 'Elon Mask'), (2, 'Tim Cook'), (3, 'Bill Gates'), (4, 'Yang Zhou')]

breakfasts = ["eggs", "toast", "banana"]
lunches = ["sushi", "pasta", "pizza"]
dinners = ["steak", "meatballs", "omlet"]

for breakfast, lunch, dinner in zip(breakfasts, dinners, lunches):
    print(f"My meal for today is {breakfast} and {lunch} and {dinner}.")
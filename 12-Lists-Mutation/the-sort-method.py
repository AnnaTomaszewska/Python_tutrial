#list.sort(*, key=None, reverse=False)
#Sortuje elementy listy w miejscu (argumenty mogą służyć do dostosowania sortowania

temperatures = [35, 48, 39, 37, 40]
temperatures.sort()
print(temperatures)

#jak dodamy po sort revers to nam owdróci posortowane

temperatures = [35, 48, 39, 37, 40]
temperatures.sort()
temperatures.reverse()
print(temperatures)

#sortuje też alfabetycznie
#jeśli są małe i duże litery to zacznie od dużych

#można też krócej:

temperatures = [35, 48, 39, 37, 40]
print(sorted(temperatures))
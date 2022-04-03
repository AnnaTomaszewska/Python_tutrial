a = { 1, 2, 4}
b = { 1, 2, 4, 5, 6}

print(a.issubset(b)) # a zawiera się w b
print(a < b)
print(a <= b)
print(b.issubset(a))

print(b.issuperset(a)) # b zawiera a i ma dodatkowe wartości
print(b > a)
print(b >= a)
print(a.issuperset(b))
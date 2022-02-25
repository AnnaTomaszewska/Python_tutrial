from re import A


a = 4
b = a

a = 6
print(a) # tu będzie 6
print(b) # tu zostanie 4, bo nie dopisaliśmy ponownie, że b = a. 

a = [1, 2, 3]
b = a

a.append(4)
print(a)
print(b)

b.append(5)
print(a)
print(b)
print("To będzie new tego dnia, \nchcę, aby to było \nw trzech liniach")
#\n przenosi kolejne wyrazy do następnej linii

print("\tPewnego dnia")
#\t działa jak tabulator

print("\"Być albo nie być\", powiedział Hamlet")
#w tym przypadku "\" działa tak aby Python nie traktował podwójnych
#""...."" jako dwa kody (tak samo jest z ''...'')

file_name = r"D:\new\trawel"
print(file_name)
# "r" działa tak, aby Python nie traktował \n lub \t jako polecenia

jakas_cyfra = 7
jakas_troche_dluzsza_cyfra = 100
bardzo_naprawde_bardzo_długa_cyfra = 12908

final = jakas_cyfra + \
        jakas_troche_dluzsza_cyfra + \
        bardzo_naprawde_bardzo_długa_cyfra

print(jakas_cyfra, 
    jakas_troche_dluzsza_cyfra, 
    bardzo_naprawde_bardzo_długa_cyfra)

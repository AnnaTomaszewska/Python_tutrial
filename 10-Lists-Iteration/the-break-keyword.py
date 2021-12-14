# funkcja break to przerwanie pętli
#możemy zastosować np do szukania czgoś w danej liście

print(3 in [1, 2, 3, 4, 4])
#lub:

def contains(values, target): #target to to, czego szukamy
    for value in values:
        if value == target:
            found = True
            break
    return found 

print(contains([1, 2, 3, 4, 5, 6], 5))
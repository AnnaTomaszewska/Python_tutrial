# Moduł Python sys zapewnia dostęp do dowolnych argumentów 
# wiersza poleceń za pomocą  metody sys.argv . 
# Służy dwóm celom:
# sys.argv to lista wszystkich argumentów wiersza poleceń.
# len(sys.argv) to całkowita liczba argumentów wiersza poleceń.

import sys
word_lenghts = 0

for arg in sys.argv[1:]:
    word_lenghts += len(arg)

print(f"Total value in my command-line arg is {word_lenghts}")

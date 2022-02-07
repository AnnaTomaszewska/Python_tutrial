adress = ["Polska", "Przasnysz", "Krótka 10",]

print(", ".join(adress))

print("-".join(["784", "367", "974"]))

# Define a word_lengths function that accepts a string. 
# It should return a list with the lengths of each word.
#
# EXAMPLES
# word_lengths("Mary Poppins was a nanny")  => [4, 7, 3, 1, 5]
# word_lengths("Somebody stole my donut")   => [8, 5, 2, 5]

def word_lenghts(word):
    words = word.split(", ")
    lenghts = []

    for word in words:
        lenghts.append(len(word))
        
    return lenghts



# Define a cleanup function that accepts a list of strings.
# The function should return the strings joined together by a space.
# There's one BIG problem -- some of the strings are empty or only consist of spaces!
# These should NOT be included in the final string
#
# cleanup(["cat", "er", "pillar"])           => "cat er pillar"
# cleanup(["cat", " ", "er", "", "pillar"])  => "cat er pillar"
# cleanup(["", "", " "])                     => ""

def cleanup(lists):
    clean_lists = []

    for list in lists:
        if list.isspace() or len(list) == 0:
            continue

        clean_lists.append(list)

    return " ".join(clean_lists)

print(cleanup(["cat", "er", "pillar"]))
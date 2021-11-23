#def count_down_from(number):
#    start = number
#    while number > 0:
#        print(start)
#        start -= 1
#
#count_down_from(6)

def count_down_from(number):
    if number  <= 0:
        return
    print(number)
    count_down_from(number - 1)

count_down_from(9)
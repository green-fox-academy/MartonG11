# create a function that takes a number,
# divides ten with it,
# and prints the result.
# it should print "fail" if the parameter is 0

import random

my_number = random.randint(0, 100)

def random_divider(number):
    try:
        print(10 / number)
    except ZeroDivisionError: 
        print("You can't divide with ZERO!")



random_divider(my_number)


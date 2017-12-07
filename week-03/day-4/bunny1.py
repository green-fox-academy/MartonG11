# We have a number of bunnies and each bunny has two big floppy ears.
# We want to compute the total number of ears across all the bunnies recursively (without loops or multiplication).


def ear_calculator(number_of_bunnies):
    if number_of_bunnies == 0:
        return 0
    elif number_of_bunnies == 1:
        return 2
    else:
        return 2 + ear_calculator((number_of_bunnies)-1)

print(ear_calculator(11))
# Write a recursive function that takes one parameter: n and counts down from n.


def counter(number):
    if number >= 0:
        counter(number - 1)
        print(number)

counter(10)
# Create a function called `odd_average` that takes a list of numbers as parameter
# and returns the average value of the odd numbers in the list
# Create basic unit tests for it with at least 3 different test cases

lista = [1,2,3,4,5]

def odd_average(input_list):
    odd_list = []
    for i in input_list:
        if i % 2 != 0:
            odd_list.append(i)
    return sum(odd_list) / len(odd_list)

print(odd_average(lista))
# - Create an array variable named `ag`
#   with the following content: `[3, 4, 5, 6, 7]`
# - Double all the values in the array

ag =[3, 4, 5, 6, 7]

def double(x):
    for i in range(len(x)):
        x[i] *= 2
    print(x)

double(ag)
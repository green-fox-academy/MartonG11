# - Create a variable named `abc`
#   with the following content: `["first", "second", "third"]`
# - Swap the first and the third element of `abc`

abc = ["first", "second", "third"]

def swap(x):
    x[0] , x[2] = x[2] , x[0]
    print(x)

swap(abc)
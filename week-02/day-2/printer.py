# - Create a function called `printer`
#   which prints the input parameters
#   (can have multiple number of arguments)

def foo(*therest):
    print(therest)

foo()
foo(1)
foo(1,2,3,4,5)

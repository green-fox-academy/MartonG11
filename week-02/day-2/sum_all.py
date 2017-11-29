# - Create a variable named `ai`
#   with the following content: `[3, 4, 5, 6, 7]`
# - Print the sum of the elements in `ai`

ai =[ 3, 4, 5, 6, 7]

def summa(x):
    total=0
    for i in range(len(x)):
        total+= x[i]
        
    print(summa(ai))
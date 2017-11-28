# - Create a variable named `p1`
#   with the following content: `[1, 2, 3]`
# - Create a variable named `p2`
#   with the following content: `[4, 5]`
# - Print if `p2` has more elements than `p1`


p1 =[1, 2, 3]
p2 =[4, 5]

def compare(x,y):
    if len(x) < len(y):
        print(y)
    

compare(p1,p2)
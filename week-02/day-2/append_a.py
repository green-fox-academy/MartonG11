# - Create a variable named `am` and assign the value `kuty` to it
# - Write a function called `appendA` that gets a string as an input
#   and appends an 'a' character to its end
# - Print the result of `appendA(am)`

am = "kuty"
def appendA(name):
    return(name + "a")
print(appendA(am))

# - Create a variable named `nimals`
#   with the following content: `["kuty", "macsk", "cic"]`
# - Add all elements an `"a"` at the end

nimals= ["kuty", "macsk", "cic"]

def appendAA(x):
    for i in range(len(x)):
        x[i]+="a"
    print(x)

appendAA(nimals)

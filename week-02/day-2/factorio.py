# - Create a function called `factorio`
#   that returns it's input's factorial

def factorio(x):
    if x == 0:
        return 1
    else:
        return x * factorio(x-1)

print(factorio(4))
print(factorio(5))
print(factorio(1))
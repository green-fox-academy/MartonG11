# Given base and n that are both 1 or more, compute recursively (no loops)
# the value of base to the n power, so powerN(3, 2) is 9 (3 squared).

def Power(n,base):
    if base == 0:
        return 1
    elif base == 1:
        return n
    else:
        return n * Power(n, base - 1)

print(Power(3, 2))


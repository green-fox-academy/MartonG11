L5=[1,2,3,4,5]
L4=[1,2,3,4]
L3=[1,2,3]
L2=[1,2]
L1=[1]
E=[]

def test(lis):
    print('whole list',lis)
    print('last item',lis[-1:])
    print('last item, step by 2',lis[-1::2])
    print('except first',lis[1:])
    print('except first, step by 2',lis[1::2])
    print('except last',lis[:-1])
    print('except last, step by 2',lis[:-1:2])
    print('except first and last',lis[1:-1])
    print('except first and last, step by 2',lis[1:-1:2])
    print('first item',lis[0:1])
    print('first item, step by 2',lis[0:1:2])
    print()

test(L5)
test(L4)
test(L3)
test(L2)
test(L1)
test(E)


print('manual slicing')
print()
first,*other,last = L5
print(first)
print(other)
print(last)

print()
first,second,*other,last = L5
print(first)
print(second)
print(other)
print(last)

print()
first,second,*other,second_to_last,last = L5
print(first)
print(second)
print(other)
print(second_to_last)
print(last)

print()
first,*other,last = L2
print(first)
print(other)
print(last)

'''
 This is not working
'''
# print()
# first,*other,last = L1
# print(first)
# print(other)
# print(last)
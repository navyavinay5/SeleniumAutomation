import itertools
l1=[1,2,3]
l2=[5,2,1]

l=sorted([i for i in itertools.chain(l1, l2)])
print(l)


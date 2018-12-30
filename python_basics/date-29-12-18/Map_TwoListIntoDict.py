l1=[1,2,3,4]
l2=['a','b','c','d']
d={x:y for x,y in zip(map(int,l1),map(str,l2))}
print(d)
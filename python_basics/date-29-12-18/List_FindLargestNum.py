#WAP to find the largest number in a list
l=[7,9,3,7]

#method1
l1=[3,8,2,9,3,20]
print(max(l1))

#method2
maxi=l[0]
for i in l:
    if i>maxi:
        maxi=i
print(maxi)


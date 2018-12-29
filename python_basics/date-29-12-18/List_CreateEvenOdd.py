#WAP to put even and odd elements in a list into two different list
l=[3,9,6,8,5,4,7]
even=[]
odd=[]
for i in l:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)
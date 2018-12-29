l=[1,4,1,4,6,8]
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)

print(l1)

#using list comprehension
[l1.append(i) for i in l if i not in l1]
print(l1)

#method2
s=(set(l))
print(s)

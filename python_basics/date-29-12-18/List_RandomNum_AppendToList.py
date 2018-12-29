#WAP to generate random numbers from 1 to 20 append them to the list

import random as r
l=[]

for i in range(1,11):
    l.append(r.randint(1,20))
print(l)

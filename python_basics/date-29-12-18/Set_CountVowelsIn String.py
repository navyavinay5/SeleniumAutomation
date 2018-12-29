#WAP to count the num of vowels present in a string using Set

s={'hi','hello'}
l=set('aeiou')
count=0
for i in s:
    for j in i:
        if j in l:
            count+=1
print("the number of vowels in given string", +count)
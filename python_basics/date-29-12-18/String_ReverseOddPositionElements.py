#wap to reverse the words of odd index value in a string
string1="hi navya how are you"
l=[]
words=string1.split()
for i in range(len(words)):
    if i%2!=0:
        str=words[i]
        l.append(str[::-1])
    else:
        l.append(words[i])
print(l)
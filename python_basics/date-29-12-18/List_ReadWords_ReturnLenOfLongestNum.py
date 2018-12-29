#WAP to read the list of words and return the length of longest one
n=int(input("enter the number of words in list"))
words=[]
wordslen=[]
for i in range(n):
    w=input("enter each word")
    words.append(w)
    wordslen.append(len(w))

print(words)
print(max(wordslen))

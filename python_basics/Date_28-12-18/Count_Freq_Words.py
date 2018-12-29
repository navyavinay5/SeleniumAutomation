str="hi navya hi hello"
d=dict()
words=str.split()

for i in words:
    w=words.count(i)
    d.setdefault(i,w)

print(d)

#using dict comprehension
di={i:words.count(i) for i in  words}
print(di)


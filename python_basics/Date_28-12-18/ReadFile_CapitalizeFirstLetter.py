f=open("file2.txt","r")
for lines in f:
    words=lines.split()
    for i in words:
        print(i.title(),end=" ")
    print()

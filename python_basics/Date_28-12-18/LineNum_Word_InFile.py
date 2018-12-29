f=open("file1.txt","r")
searchWord="this"
count=1
for lines in f:
    if searchWord in lines:
        print(count)
    count+=1




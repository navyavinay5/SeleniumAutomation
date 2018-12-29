f=open("file1.txt","r")
for lines in reversed(list(f)):
    print(lines)
f.close()

#print(lines.rstrip()) if we ise this then the output will be displayed without spaces
try:
    f=open("file1.txt",'r')
    f.write("Hi")
except Exception as e:
    print(type(e))
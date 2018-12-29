string1=input("Enter the first string:")
string2=input("Enter the Second string:")
interset=set(set(string1)&set(string2))
if len(interset)>0:
    print("Common letters present in two input strings")
print(interset)
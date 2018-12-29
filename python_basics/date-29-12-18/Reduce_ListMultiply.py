import functools as f
l = [1,2,3,4]
output=f.reduce(lambda a,b:a*b,l)
print(output)
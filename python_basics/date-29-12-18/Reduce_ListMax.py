import functools as f
l = [90,45,100,5]
output=f.reduce(lambda x,y:x if x>y else y,l)
print(output)
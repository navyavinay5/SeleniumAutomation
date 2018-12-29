try:
    s=(1,2,3)
    i = iter(s)
    print (next(i))
    print (next(i))
    print (next(i))
    print (next(i))
except Exception as e:
    print (type(e))
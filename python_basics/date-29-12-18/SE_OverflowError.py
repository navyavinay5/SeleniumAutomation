try:
    c=1
    d=2.0**c
    for i in range(10):
        print(i)
        d=d**2
except Exception as E:
    print(type(E))
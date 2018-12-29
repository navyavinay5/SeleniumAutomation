try :
    n = int(input("Enter the number"))
    output= n / 0
    print(output)
except Exception as e:
    print(type(e))
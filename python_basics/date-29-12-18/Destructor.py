class A():
    def __init__(self):
        print("Its constructor")
    def __del__(self):
        print("Its destructor")
obj=A()
del obj

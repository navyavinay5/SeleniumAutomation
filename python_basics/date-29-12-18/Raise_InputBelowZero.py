class NegativeNumberException(Exception):
    pass
class Number():
    n=int(input("enter a number"))
    if n<0:
        raise NegativeNumberException
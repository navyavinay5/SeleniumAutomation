import math
for number in range(1,40):
    square=int(math.sqrt(number))
    if number == square*square:
        print(number)
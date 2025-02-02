import sys

while True:
    number1, number2 = [int(num) for num in sys.stdin.readline().split()]
    if number1 == number2 == 0:
        break
    elif number2 % number1 == 0:
        print("factor")
    elif number1 % number2 == 0:
        print("multiple")
    else:
        print("neither")

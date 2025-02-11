import sys

N = int(sys.stdin.readline())


def is_prime(number):
    if number <= 1:
        return False
    root_square = number ** (1 / 2)
    divisor = 2
    while divisor <= root_square:
        if number % divisor == 0:
            return False
        divisor += 1
    return True


for _ in range(N):
    number = int(sys.stdin.readline())
    while not is_prime(number):
        number += 1
    print(number)

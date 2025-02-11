primes = []

M, N = [int(num) for num in input().split()]


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


for number in range(M, N + 1):
    if is_prime(number):
        primes.append(number)

print(*primes, sep="\n")

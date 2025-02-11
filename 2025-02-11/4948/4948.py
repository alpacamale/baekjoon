import sys


def is_prime(number):
    if number == 1:
        return False
    for divisor in range(2, int(number ** (1 / 2)) + 1):
        if number % divisor == 0:
            return False
    return True


numbers = []
while True:
    number = int(sys.stdin.readline())
    if number == 0:
        break
    numbers.append(number)
start = min(numbers)
primes = [2] if start == 2 else []
if start % 2 == 0:
    start += 1
end = max(numbers) * 2 + 1
for number in range(start, end):
    if is_prime(number):
        primes.append(number)

for number in numbers:
    length = len([prime for prime in primes if number < prime <= number * 2])
    print(length)

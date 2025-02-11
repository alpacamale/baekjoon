import sys

numbers = [int(num) for num in sys.stdin.read().split()[1:]]
end = max(numbers) + 1
primes = [True] * end
primes[0] = primes[1] = False

for number in range(2, int(end**0.5) + 1):
    if primes[number]:
        for composite in range(2 * number, end, number):
            primes[composite] = False

primes = [index for index, value in enumerate(primes) if value]
prime_set = set(primes)

for number in numbers:
    total = 0
    for prime in primes:
        end = number // 2
        if prime > end:
            break
        if number - prime in prime_set:
            total += 1
    print(total)

M = int(input())
N = int(input())
prime_numbers = []
M = max(2, M)
for number in range(M, N + 1):
    is_prime = True
    for divisor in range(2, int(number ** (1 / 2)) + 1):
        quotient, remains = divmod(number, divisor)
        if remains == 0:
            is_prime = False
            break
    if is_prime:
        prime_numbers.append(number)
if not prime_numbers:
    print(-1)
else:
    print(sum(prime_numbers), min(prime_numbers), sep="\n")

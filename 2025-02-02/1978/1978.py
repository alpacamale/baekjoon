input()
numbers = [int(num) for num in input().split()]

result = 0
for number in numbers:
    divisors = {1, number}
    for divisor in range(2, int(number ** (1 / 2) + 1)):
        quotient, remains = divmod(number, divisor)
        if remains == 0:
            divisors.update([quotient, divisor])
    if len(divisors) == 2:
        result += 1
print(result)

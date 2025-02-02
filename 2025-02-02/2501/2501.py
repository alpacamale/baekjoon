N, K = [int(num) for num in input().split()]
divisors = {1, N}
end = int(N ** (1 / 2)) + 1
for number in range(2, end):
    quotient, remains = divmod(N, number)
    if remains == 0:
        divisors.update([number, quotient])
if len(divisors) < K:
    print(0)
else:
    divisors = list(divisors)
    divisors.sort()
    print(divisors[K - 1])

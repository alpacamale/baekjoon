numer_a, denom_a = [int(num) for num in input().split()]
numer_b, denom_b = [int(num) for num in input().split()]
c = denom_a * denom_b
a, b = denom_a, denom_b
while b != 0:
    a, b = b, a % b

denom_c = c // a
numer_c = numer_a * (denom_c // denom_a) + numer_b * (denom_c // denom_b)
a, b = numer_c, denom_c
while b != 0:
    a, b = b, a % b
print(numer_c // a, denom_c // a)

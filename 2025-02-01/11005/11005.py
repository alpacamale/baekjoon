N, B = [int(num) for num in input().split()]

remainders = []
while N != 0:
    N, mod = divmod(N, B)
    remainders.append(mod)

numeral = (
    "".join(chr(num + 55) if num >= 10 else str(num) for num in remainders[::-1]) or "0"
)
print(numeral)

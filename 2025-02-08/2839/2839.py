N = int(input())
result = -1
for number in range(N // 5, -1, -1):
    remain = N - (number * 5)
    quotient, remain = divmod(remain, 3)
    if remain == 0:
        result = number + quotient
        break
print(result)

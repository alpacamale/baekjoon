N = [int(num) for num in input()]
numbers = sorted(N, key=lambda x: -x)
print(*numbers, sep="")

N = int(input())

for n in range(N):
    print(" " * (N - n - 1), "*" * (1 + (n * 2)), sep="")
for n in range(N - 2, -1, -1):
    print(" " * (N - n - 1), "*" * (1 + (n * 2)), sep="")

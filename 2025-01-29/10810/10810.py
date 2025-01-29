N, M = [int(num) for num in input().split()]
baskets = ["0" for _ in range(N)]
for _ in range(M):
    i, j, k = [int(num) for num in input().split()]
    baskets[i - 1 : j] = [str(k) for _ in range(j - i + 1)]
print(" ".join(baskets))

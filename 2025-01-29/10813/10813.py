N, M = [int(num) for num in input().split()]
baskets = [str(num) for num in range(1, N + 1)]
for _ in range(M):
    i, j = [int(num) for num in input().split()]
    baskets[i - 1], baskets[j - 1] = baskets[j - 1], baskets[i - 1]
print(" ".join(baskets))

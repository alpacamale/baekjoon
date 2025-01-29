T = int(input())

for t in range(1, T + 1):
    A, B = [int(num) for num in input().split()]
    print(f"Case #{t}: {A + B}")

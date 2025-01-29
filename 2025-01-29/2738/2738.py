N, M = [int(num) for num in input().split()]

matrix1 = [[int(num) for num in input().split()] for _ in range(N)]
matrix2 = [[int(num) for num in input().split()] for _ in range(N)]
for row1, row2 in zip(matrix1, matrix2):
    print(*[a + b for a, b in zip(row1, row2)])

matrix = [[0] * 100 for _ in range(100)]
N = int(input())
for _ in range(N):
    x, y = [int(num) for num in input().split()]
    for row in range(x, x + 10):
        matrix[row][y : y + 10] = [1] * 10
print(sum(col for row in matrix for col in row if col == 1))

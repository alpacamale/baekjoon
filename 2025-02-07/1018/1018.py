import sys

N, M = [int(num) for num in sys.stdin.readline().split()]
sum_rows = []
result = 64
for line in sys.stdin.readlines():
    sum_row = []
    for row_start in range(M - 7):
        row_end = row_start + 8
        sum_row.append(
            sum(
                1
                for cindex, color in enumerate(line[row_start:row_end])
                if ((len(sum_rows) + cindex) % 2 == 0 and color == "W")
                or ((len(sum_rows) + cindex) % 2 == 1 and color == "B")
            )
        )
    sum_rows.append(sum_row)
# print(sum_rows)

sum_matrix = []
for cindex in range(M - 7):
    for row_start in range(N - 7):
        row_end = row_start + 8
        sum_cols = [sum(row) for row in zip(*sum_rows[row_start:row_end])]
        sum_matrix.extend(sum_cols)
# print(sum_matrix)
print(min(64 - max(sum_matrix), min(sum_matrix)))

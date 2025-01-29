import sys

numbers = [int(num) for num in sys.stdin.read().replace("\n", " ").split()]
max_num = max(numbers)
index = numbers.index(max_num)
row = index // 9 + 1
col = index % 9 + 1
print(max_num)
print(row, col)

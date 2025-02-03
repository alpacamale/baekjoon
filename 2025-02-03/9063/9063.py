import sys

N = int(sys.stdin.readline())
x_list = []
y_list = []
for _ in range(N):
    x, y = [int(num) for num in sys.stdin.readline().split()]
    x_list.append(x)
    y_list.append(y)
print((max(x_list) - min(x_list)) * (max(y_list) - min(y_list)))

import sys

N = int(sys.stdin.readline())
dots = [[int(num) for num in line.split()] for line in sys.stdin.read().split("\n")]
dots = sorted(dots, key=lambda x: (x[0], x[1]))
for x, y in dots:
    print(x, y)

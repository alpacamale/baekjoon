import sys

times = int(sys.stdin.readline())

for time in range(times):
    A, B = [int(num) for num in sys.stdin.readline().split()]
    print(A + B)

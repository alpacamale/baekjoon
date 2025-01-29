import sys

for line in sys.stdin:
    A, B = [int(num) for num in line.split()]
    print(A + B)

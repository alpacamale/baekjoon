import sys

A, B = [int(num) for num in sys.stdin.readline().split()]
C = A * B
while B != 0:
    A, B = B, A % B
print(C // A)

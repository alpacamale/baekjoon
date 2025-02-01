import math

A, B, V = [int(num) for num in input().split()]

days = math.ceil((V - A) / (A - B) + 1)
print(days)

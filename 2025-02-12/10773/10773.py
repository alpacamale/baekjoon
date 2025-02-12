import sys

numbers = []

K = int(sys.stdin.readline())
for _ in range(K):
    number = int(sys.stdin.readline())
    if number != 0:
        numbers.append(number)
    else:
        numbers.pop()
print(sum(numbers))

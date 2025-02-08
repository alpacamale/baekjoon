import sys

numbers = [int(num) for num in sys.stdin.read().split()[1:]]
print(*sorted(numbers), sep="\n")

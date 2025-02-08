import sys

numbers = [int(number) for number in sys.stdin.read().split()[1:]]
for number in sorted(numbers):
    print(number)

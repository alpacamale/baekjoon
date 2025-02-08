import sys

numbers = [int(num) for num in sys.stdin.read().split()]
print(sum(numbers) // 5, sorted(numbers)[2], sep="\n")

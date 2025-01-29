import sys

count = set(int(num) % 42 for num in sys.stdin.readlines())
print(len(count))

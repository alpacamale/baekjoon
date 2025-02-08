import sys

N = int(sys.stdin.readline())
counts = [0] * 10001

while True:
    number = sys.stdin.readline()
    if not number:
        break
    counts[int(number)] += 1

for index, count in enumerate(counts):
    for _ in range(count):
        print(index)

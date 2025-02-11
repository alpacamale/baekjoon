import sys


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


N = int(sys.stdin.readline())
intervals = set()
distances = []
for _ in range(N):
    distance = int(sys.stdin.readline())
    if len(distances) != 0:
        intervals.add(distance - distances[-1])
    distances.append(distance)

intervals = list(intervals)
g = 0
for index in range(len(intervals) - 1):
    if g == 0:
        g = gcd(intervals[index], intervals[index + 1])
    else:
        g = gcd(g, intervals[index + 1])

if g == 0:
    print(0)
else:
    print(len(range(distances[0], distances[-1] + 1, g)) - len(distances))

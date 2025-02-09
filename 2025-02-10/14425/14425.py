import sys

N, M = [int(num) for num in input().split()]

word_set = set()
for _ in range(N):
    word_set.add(sys.stdin.readline().rstrip())
words = [word.rstrip() for word in sys.stdin.readlines()]
print(sum(1 for word in words if word in word_set))

import sys

N = int(sys.stdin.readline())
words = set()
for _ in range(N):
    words.add(sys.stdin.readline().rstrip())
words = list(words)
words.sort(key=lambda x: (len(x), x))
print(*words, sep="\n")

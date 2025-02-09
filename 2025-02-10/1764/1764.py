import sys

N, M = [int(num) for num in sys.stdin.readline().split()]
never_heard = set()
never_seen = set()
for _ in range(N):
    name = sys.stdin.readline().rstrip()
    never_heard.add(name)
for _ in range(M):
    name = sys.stdin.readline().rstrip()
    never_seen.add(name)

never_heard_and_seen = list(never_heard & never_seen)
never_heard_and_seen.sort()
print(len(never_heard_and_seen), *never_heard_and_seen, sep="\n")

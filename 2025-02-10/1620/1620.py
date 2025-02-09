import sys

N, M = [int(num) for num in sys.stdin.readline().split()]

name_to_index = {}
index_to_name = {}

for index in range(1, N + 1):
    name = sys.stdin.readline().rstrip()
    name_to_index[name] = index
    index_to_name[index] = name

for _ in range(M):
    key = sys.stdin.readline().rstrip()
    if key.isdigit():
        print(index_to_name[int(key)])
    else:
        print(name_to_index[key])

line = int(input())

for l in range(1, line + 1):
    print(" " * (line - l) + "*" * l)

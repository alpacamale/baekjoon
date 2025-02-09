import sys

N = int(sys.stdin.readline())
employees = set()
for _ in range(N):
    name, log = sys.stdin.readline().split()
    if log == "enter":
        employees.add(name)
    else:
        employees.remove(name)
employees = list(employees)
employees.sort(reverse=True)
print(*employees, sep="\n")

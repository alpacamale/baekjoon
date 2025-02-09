import sys

N = int(sys.stdin.readline())

people = []
for _ in range(N):
    age, name = sys.stdin.readline().split()
    age = int(age)
    people.append([age, name])
people.sort(key=lambda x: x[0])
people = [f"{age} {name}" for age, name in people]
print(*people, sep="\n")

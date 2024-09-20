length = input()
numbers = (int(x) for x in input().split())
min_number = 1000000
max_number = -1000000

for number in numbers:
    min_number = min(min_number, number)
    max_number = max(max_number, number)

print(min_number, max_number)

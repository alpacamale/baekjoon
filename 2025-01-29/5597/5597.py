import sys

numbers = set(range(1, 31))
attendence = set(int(num) for num in sys.stdin.readlines())
not_attendence = numbers - attendence
print(min(not_attendence))
print(max(not_attendence))

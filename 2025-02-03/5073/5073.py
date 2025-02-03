import sys

while True:
    lines = [int(num) for num in sys.stdin.readline().split()]
    longest = max(lines)
    total = sum(lines)
    if total == 0:
        break
    elif total - longest <= longest:
        print("Invalid")
    elif total == 3 * longest:
        print("Equilateral")
    elif total - 2 * longest == min(lines) or total - 2 * min(lines) == longest:
        print("Isosceles")
    else:
        print("Scalene")

lines = [int(num) for num in input().split()]
longest = max(lines)
total = sum(lines)
if total - longest <= longest:
    total = (total - longest) * 2 - 1
print(total)

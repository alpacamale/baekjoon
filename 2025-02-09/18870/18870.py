N = int(input())
numbers = [int(num) for num in input().split()]
ordered = {number: index for index, number in enumerate(sorted(list(set(numbers))))}
result = [ordered[number] for number in numbers]
print(*result, sep=" ")

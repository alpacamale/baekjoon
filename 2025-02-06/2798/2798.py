N, M = [int(num) for num in input().split()]
numbers = [int(num) for num in input().split()]
length = len(numbers)
max_number = 0
for i in range(length - 2):
    for j in range(i + 1, length - 1):
        for k in range(j + 1, length):
            if numbers[i] + numbers[j] + numbers[k] <= M:
                max_number = max(max_number, numbers[i] + numbers[j] + numbers[k])
print(max_number)

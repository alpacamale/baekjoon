N, k = [int(num) for num in input().split()]
numbers = [int(num) for num in input().split()]
print(sorted(numbers, key=lambda x: -x)[k - 1])

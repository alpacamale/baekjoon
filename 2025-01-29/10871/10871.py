X = int(input().split()[1])
numbers = [num for num in input().split() if int(num) < X]
print(" ".join(numbers))

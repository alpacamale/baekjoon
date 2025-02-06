N = int(input())
result = 0
for number in range(1, N + 1):
    generator = number + sum(int(char) for char in str(number))
    if generator == N:
        result = number
        break
print(result)

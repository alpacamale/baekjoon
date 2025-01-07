max_number = max_index = 0
for times in range(9):
    number = int(input())
    if number > max_number:
        max_number = number
        max_index = times + 1
print(max_number)
print(max_index)

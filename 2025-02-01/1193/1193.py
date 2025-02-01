X = int(input())
total = 2
while X > total * (total - 1) // 2:
    total += 1

number1 = total - X + (total - 1) * (total - 2) // 2
number2 = total - number1
if total % 2 == 0:
    print(number1, number2, sep="/")
else:
    print(number2, number1, sep="/")

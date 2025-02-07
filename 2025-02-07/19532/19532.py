a, b, c, d, e, f = [int(num) for num in input().split()]
finish = False
for x in range(1000):
    if finish:
        break
    for y in range(1000):
        if finish:
            break
        if a * x + b * y == c and d * x + e * y == f:
            print(x, y)
            finish = True
        elif a * x + b * y * -1 == c and d * x + e * y * -1 == f:
            print(x, y * -1)
            finish = True
        elif a * x * -1 + b * y == c and d * x * -1 + e * y == f:
            print(x * -1, y)
            finish = True
        elif a * x * -1 + b * y * -1 == c and d * x * -1 + e * y * -1 == f:
            print(x * -1, y * -1)
            finish = True

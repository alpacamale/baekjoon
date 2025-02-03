x, y, w, h = [int(num) for num in input().split()]
print(min(min(x, w - x), min(y, h - y)))

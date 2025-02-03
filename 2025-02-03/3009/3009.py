x_coordinate = {}
y_coordinate = {}
for _ in range(3):
    x, y = [int(num) for num in input().split()]
    if x_coordinate.get(x, None):
        del x_coordinate[x]
    else:
        x_coordinate[x] = True
    if y_coordinate.get(y, None):
        del y_coordinate[y]
    else:
        y_coordinate[y] = True
print(list(x_coordinate.keys())[0], list(y_coordinate.keys())[0])

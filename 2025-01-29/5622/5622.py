dials = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
string = input()
time = 0
for char in string:
    for index, dial in enumerate(dials):
        if char in dial:
            time += index + 3
print(time)

string = input()
result = ["-1"] * 26
for index, char in enumerate(string):
    code = ord(char) - 97
    if result[code] == "-1":
        result[code] = str(index)
print(" ".join(result))

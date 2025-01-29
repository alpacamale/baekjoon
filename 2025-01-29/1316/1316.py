def is_group(string):
    before = ""
    for char in string:
        if char not in before:
            before += char
        elif char in before and char != before[-1]:
            return False
    return True


N = int(input())
result = 0
for _ in range(N):
    string = input()
    if is_group(string):
        result += 1
print(result)

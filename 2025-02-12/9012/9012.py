import sys

T = int(sys.stdin.readline())
for _ in range(T):
    parenthesis = []
    strings = sys.stdin.readline().rstrip()
    answer = "YES"
    for char in strings:
        if char == "(":
            parenthesis.append(char)
        elif char == ")" and parenthesis and parenthesis[-1] == "(":
            parenthesis.pop()
        else:
            answer = "NO"
            break
    if parenthesis:
        answer = "NO"

    print(answer)

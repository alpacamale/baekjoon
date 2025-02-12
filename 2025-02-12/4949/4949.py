import sys

for strings in sys.stdin.read().split("\n"):
    if strings == ".":
        break
    stack = []
    result = "yes"
    for char in strings:
        if char in ("(", "["):
            stack.append(char)
        elif (
            char == ")"
            and stack
            and stack[-1] == "("
            or char == "]"
            and stack
            and stack[-1] == "["
        ):
            stack.pop()
        elif (
            char in (")", "]")
            and not stack
            or char == ")"
            and stack[-1] != "("
            or char == "]"
            and stack[-1] != "["
        ):
            result = "no"
            break
    if stack:
        result = "no"
    print(result)

import sys

N = int(sys.stdin.readline())
sequence = [int(num) for num in sys.stdin.readline().split()][::-1]
stack = []
order = 1

while order < N + 1:
    if sequence and sequence[-1] == order:
        sequence.pop()
        order += 1
    elif stack and stack[-1] == order:
        stack.pop()
        order += 1
    else:
        if sequence:
            stack.append(sequence.pop())
        else:
            break

print("Nice" if not stack else "Sad")

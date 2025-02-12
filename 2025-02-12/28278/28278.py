import sys

stack = []

N = int(sys.stdin.readline())
for _ in range(N):
    demands = [int(num) for num in sys.stdin.readline().split()]
    demand = demands[0]
    if demand == 1:
        stack.append(demands[1])
    elif demand == 2:
        print(-1 if not stack else stack.pop())
    elif demand == 3:
        print(len(stack))
    elif demand == 4:
        print(0 if stack else 1)
    elif demand == 5:
        print(-1 if not stack else stack[-1])

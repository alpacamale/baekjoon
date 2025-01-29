T = int(input())
for _ in range(T):
    S, R = input().split()
    S = int(S)
    P = "".join(char * S for char in R)
    print(P)

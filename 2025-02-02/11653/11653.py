N = int(input())

divisor = 2
end = int(N ** (1 / 2)) + 1
while N != 1:
    quotient, remains = divmod(N, divisor)
    if remains == 0:
        print(divisor)
        N = quotient
        end = int(N ** (1 / 2)) + 1
    else:
        if divisor == end:
            print(N)
            break
        divisor += 1

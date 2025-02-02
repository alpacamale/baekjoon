import sys

while True:
    n = int(sys.stdin.readline())
    if n == -1:
        break
    divisors = {1}
    end = int(n ** (1 / 2)) + 1
    for num in range(2, end):
        quotient, remains = divmod(n, num)
        if remains == 0:
            divisors.update([quotient, num])
    message = (
        f"{n} is NOT perfect."
        if sum(divisors) != n
        else f"{n} = {" + ".join(str(num) for num in sorted(list(divisors)))}"
    )
    print(message)

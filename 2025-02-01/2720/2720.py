T = int(input())

for _ in range(T):
    cents = int(input())
    quarter, remain = divmod(cents, 25)
    dime, remain = divmod(remain, 10)
    nickel, penny = divmod(remain, 5)
    print(quarter, dime, nickel, penny)

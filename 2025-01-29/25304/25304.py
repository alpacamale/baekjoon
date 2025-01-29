total = int(input())
types = int(input())

for _ in range(types):
    price, quantity = [int(num) for num in input().split()]
    total -= price * quantity

if total == 0:
    print("Yes")
else:
    print("No")

input()
counter = {}
for card in input().split():
    if counter.get(card):
        counter[card] += 1
    else:
        counter[card] = 1
input()
counts = [counter.get(card, 0) for card in input().split()]
print(*counts)

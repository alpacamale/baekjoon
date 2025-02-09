input()
deck = set(input().split())
input()
result = [1 if card in deck else 0 for card in input().split()]
print(*result)

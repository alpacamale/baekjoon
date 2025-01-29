from itertools import zip_longest

arr = [input().strip() for _ in range(5)]
result = "".join(c for row in zip_longest(*arr, fillvalue="") for c in row)
print(result)

import numpy as np

my_deck = np.array([int(num) for num in input().split()])
default = np.array([1, 1, 2, 2, 2, 8])
print(" ".join((default - my_deck).astype(str)))

S = input()
length = len(S)
substrings = set()
for number in range(length):
    start = 0
    end = start + number + 1
    while end <= length:
        substrings.add(S[start:end])
        start += 1
        end = start + number + 1
print(len(substrings))

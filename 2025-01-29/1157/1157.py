string = input().upper()
string_counts = {}
for char in string:
    if string_counts.get(char, None):
        string_counts[char] += 1
    else:
        string_counts[char] = 1

max_count = max(string_counts.values())
if list(string_counts.values()).count(max_count) != 1:
    print("?")
else:
    print(max(string_counts, key=lambda x: string_counts[x]))

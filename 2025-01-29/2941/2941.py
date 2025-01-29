words = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

string = input()
for word in words:
    string = string.replace(word, ",")
print(len(string))

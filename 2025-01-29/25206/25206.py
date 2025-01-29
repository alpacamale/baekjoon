import sys

to_score = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0,
}

total = 0
scores = 0
for line in sys.stdin.readlines():
    _, score, grade = line.rstrip().split()
    if grade == "P":
        continue
    score = float(score)
    scores += score
    total += score * to_score[grade]
print(total / scores)

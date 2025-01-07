times = int(input())
scores = []


def runQuiz():
    string = input()
    total_point = 0
    additional_point = 0
    for c in string:
        if c == "O":
            additional_point += 1
            total_point += additional_point
        else:
            additional_point = 0
    scores.append(total_point)


for time in range(times):
    runQuiz()

for score in scores:
    print(score)

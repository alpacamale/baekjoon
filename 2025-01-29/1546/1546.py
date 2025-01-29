length = int(input())
scores = [int(num) for num in input().split()]
max_score = max(scores)
avg = sum(score / max_score * 100 for score in scores) / length
print(avg)

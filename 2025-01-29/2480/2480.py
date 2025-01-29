from collections import Counter

numbers = [int(num) for num in input().split()]
number_counts = Counter(numbers)
if len(number_counts) == 1:
    print(10000 + numbers[0] * 1000)
elif len(number_counts) == 2:
    print(1000 + number_counts.most_common(1)[0][0] * 100)
else:
    print(max(number_counts) * 100)

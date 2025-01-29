from datetime import datetime, timedelta

hour, min = [int(num) for num in input().split()]
delta = int(input())
end = datetime(2025, 1, 1, hour, min) + timedelta(minutes=delta)
hour, min = [int(num) for num in end.strftime("%H %M").split()]
print(hour, min)

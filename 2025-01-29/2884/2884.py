from datetime import datetime, timedelta

hour, min = [int(num) for num in input().split()]
alarm = datetime(2025, 1, 1, hour, min) - timedelta(minutes=45)
hour, min = [int(num) for num in alarm.strftime("%H %M").split()]
print(hour, min)

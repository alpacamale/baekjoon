# 2884

[코딩테스트 연습 - 2884][1] 로 이동

## 문제

상근이는 매일 아침 알람을 듣고 일어난다. 알람을 듣고 바로 일어나면 다행이겠지만, 항상 조금만 더 자려는 마음 때문에 매일 학교를 지각하고 있다.
상근이는 모든 방법을 동원해보았지만, 조금만 더 자려는 마음은 그 어떤 것도 없앨 수가 없었다.
이런 상근이를 불쌍하게 보던 창영이는 자신이 사용하는 방법을 추천해 주었다.
바로 "45분 일찍 알람 설정하기"이다.
이 방법은 단순하다. 원래 설정되어 있는 알람을 45분 앞서는 시간으로 바꾸는 것이다. 어차피 알람 소리를 들으면, 알람을 끄고 조금 더 잘 것이기 때문이다. 이 방법을 사용하면, 매일 아침 더 잤다는 기분을 느낄 수 있고, 학교도 지각하지 않게 된다.
현재 상근이가 설정한 알람 시각이 주어졌을 때, 창영이의 방법을 사용한다면, 이를 언제로 고쳐야 하는지 구하는 프로그램을 작성하시오.

## 입력

첫째 줄에 두 정수 H와 M이 주어진다. (0 ≤ H ≤ 23, 0 ≤ M ≤ 59) 그리고 이것은 현재 상근이가 설정한 알람 시간 H시 M분을 의미한다.

## 출력

첫째 줄에 상근이가 창영이의 방법을 사용할 때, 설정해야 하는 알람 시간을 출력한다. (입력과 같은 형태로 출력하면 된다.)

## 예제 입력

```
10 10
```

## 예제 출력

```
9 25
```

## 풀이

min이 45보다 적을 때, hour가 0일때를 생각해서 조건문을 써준다.

```python
hour, min = [int(num) for num in input().split()]

if min < 45 and hour == 0:
    hour = 23
    min = min + 15
elif min < 45:
    hour -= 1
    min = min + 15
else:
    min -= 45

print(hour, min)

```

혹은 datetime 모듈을 이용해서 풀 수도 있다.

```python
from datetime import datetime, timedelta

hour, min = [int(num) for num in input().split()]
alarm = datetime(2025, 1, 1, hour, min) - timedelta(minutes=45)
hour, min = [int(num) for num in alarm.strftime("%H %M").split()]
print(hour, min)

```

[1]: https://www.acmicpc.net/problem/2884

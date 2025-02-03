# 5073

[코딩테스트 연습 - 5073][1] 로 이동

## 문제

삼각형의 세 변의 길이가 주어질 때 변의 길이에 따라 다음과 같이 정의한다.
Equilateral :  세 변의 길이가 모두 같은 경우
Isosceles : 두 변의 길이만 같은 경우
Scalene : 세 변의 길이가 모두 다른 경우
단 주어진 세 변의 길이가 삼각형의 조건을 만족하지 못하는 경우에는 "Invalid" 를 출력한다. 예를 들어 6, 3, 2가 이 경우에 해당한다. 가장 긴 변의 길이보다 나머지 두 변의 길이의 합이 길지 않으면 삼각형의 조건을 만족하지 못한다.
세 변의 길이가 주어질 때 위 정의에 따른 결과를 출력하시오.

## 입력

각 줄에는 1,000을 넘지 않는 양의 정수 3개가 입력된다. 마지막 줄은 0 0 0이며 이 줄은 계산하지 않는다.

## 출력

각 입력에 맞는 결과 (Equilateral, Isosceles, Scalene, Invalid) 를 출력하시오.

## 예제 입력

```
7 7 7

6 5 4

3 2 5

6 2 6

0 0 0


```

## 예제 출력

```
Equilateral

Scalene

Invalid

Isosceles


```

## 풀이

변의 길이의 총합과 가장 긴 변의 차를 이용해서 나머지 변들의 길이를 유추하는 식으로 코드를 짯다.

total - longest <= longest 는 가장 긴 변의 길이를 제외한 변의 길이가 가장 긴 변의 길이와 같거나 작을때 삼각형의 조건을 만족하지 못한다.

total == 3 \* longest 는 가장 긴 변의 길이에 3을 곱한것과 total이 같다면 모든 변의 길이가 같다는 것을 의미한다.

total - 2 _ longest == min(lines) 는 큰 변의 길이가 두개일때,
total - 2 _ min(lines) == longest 는 작은 변의 길이가 두개일때,
참이다.

```python
import sys

while True:
    lines = [int(num) for num in sys.stdin.readline().split()]
    longest = max(lines)
    total = sum(lines)
    if total == 0:
        break
    elif total - longest <= longest:
        print("Invalid")
    elif total == 3 * longest:
        print("Equilateral")
    elif total - 2 * longest == min(lines) or total - 2 * min(lines) == longest:
        print("Isosceles")
    else:
        print("Scalene")

```

[1]: https://www.acmicpc.net/problem/5073

# 13909

[코딩테스트 연습 - 13909][1] 로 이동

## 문제

서강대학교 컴퓨터공학과 실습실 R912호에는 현재 N개의 창문이 있고 또 N명의 사람이 있다. 1번째 사람은 1의 배수 번째 창문을 열려 있으면 닫고 닫혀 있으면 연다.  2번째 사람은 2의 배수 번째 창문을 열려 있으면 닫고 닫혀 있으면 연다. 이러한 행동을 N번째 사람까지 진행한 후 열려 있는 창문의 개수를 구하라. 단, 처음에 모든 창문은 닫혀 있다.
예를 들어 현재 3개의 창문이 있고 3명의 사람이 있을 때,

1. 1번째 사람은 1의 배수인 1,2,3번 창문을 연다. (1, 1, 1)
2. 2번째 사람은 2의 배수인 2번 창문을 닫는다. (1, 0, 1)
3. 3번째 사람은 3의 배수인 3번 창문을 닫는다. (1, 0, 0)

결과적으로 마지막에 열려 있는 창문의 개수는 1개 이다.

## 입력

첫 번째 줄에는 창문의 개수와 사람의 수 N(1 ≤ N ≤ 2,100,000,000)이 주어진다.

## 출력

마지막에 열려 있는 창문의 개수를 출력한다.

## 예제 입력

```
3

```

## 예제 출력

```
1

```

## 풀이

약수의 배수가 짝수개면 문이 닫히고,
홀수개면 문이 열린다.
N까지의 약수의 개수를 구하면 된다.

```python
import sys

windows = 0
N = int(sys.stdin.readline())
for number in range(1, N + 1):
    divisor = 1
    divisors = set()
    while divisor <= number**0.5:
        quotient, remain = divmod(number, divisor)
        if remain == 0:
            divisors.update([divisor, quotient])
        divisor += 1
    if len(divisors) % 2 == 1:
        windows += 1
print(windows)

```

시간 초과가 나왔다.
단순하게 구해보겠다.
boolean으로 이루어진 배열을 만들고, N까지의 수를 반복하며 N의 배수 인덱스의 boolean에 not 연산을 할것이다.

```python
import sys

windows = 0
N = int(sys.stdin.readline())
windows = [True] * (N + 1)
windows[0] = False
for number in range(2, N + 1):
    for divisor in range(number, N + 1, number):
        windows[divisor] = not windows[divisor]
print(sum(windows))

```

이건 메모리 초과가 나왔다.
약수의 개수가 완전 제곱수일 경우에만 약수의 개수가 홀수이다.
1, 4, 9, 25 ...
N의 제곱근을 계산한 후, 정수수분을 출력하면 됩니다.

```python
print(int(int(input()) ** 0.5))
```

[1]: https://www.acmicpc.net/problem/13909

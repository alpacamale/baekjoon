# 4134

[코딩테스트 연습 - 4134][1] 로 이동

## 문제

정수 n(0 ≤ n ≤ 4\*109)가 주어졌을 때, n보다 크거나 같은 소수 중 가장 작은 소수 찾는 프로그램을 작성하시오.

## 입력

첫째 줄에 테스트 케이스의 개수가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n이 주어진다.

## 출력

각각의 테스트 케이스에 대해서 n보다 크거나 같은 소수 중 가장 작은 소수를 한 줄에 하나씩 출력한다.

## 예제 입력

```
3
6
20
100


```

## 예제 출력

```
7
23
101


```

## 풀이

n의 제곱근까지 n의 약수가 없다면 소수다.

```python
import sys

N = int(sys.stdin.readline())


def is_prime(number):
    if number <= 1:
        return False
    root_square = number ** (1 / 2)
    divisor = 2
    while divisor <= root_square:
        if number % divisor == 0:
            return False
        divisor += 1
    return True


for _ in range(N):
    number = int(sys.stdin.readline())
    while not is_prime(number):
        number += 1
    print(number)

```

[1]: https://www.acmicpc.net/problem/4134

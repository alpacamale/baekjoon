# 4948

[코딩테스트 연습 - 4948][1] 로 이동

## 문제

베르트랑 공준은 임의의 자연수 n에 대하여, n보다 크고, 2n보다 작거나 같은 소수는 적어도 하나 존재한다는 내용을 담고 있다.
이 명제는 조제프 베르트랑이 1845년에 추측했고, 파프누티 체비쇼프가 1850년에 증명했다.
예를 들어, 10보다 크고, 20보다 작거나 같은 소수는 4개가 있다. (11, 13, 17, 19) 또, 14보다 크고, 28보다 작거나 같은 소수는 3개가 있다. (17,19, 23)
자연수 n이 주어졌을 때, n보다 크고, 2n보다 작거나 같은 소수의 개수를 구하는 프로그램을 작성하시오.

## 입력

입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 케이스는 n을 포함하는 한 줄로 이루어져 있다.
입력의 마지막에는 0이 주어진다.

## 출력

각 테스트 케이스에 대해서, n보다 크고, 2n보다 작거나 같은 소수의 개수를 출력한다.

## 예제 입력

```
1
10
13
100
1000
10000
100000
0

```

## 예제 출력

```
1
4
3
21
135
1033
8392

```

## 풀이

n부터 2n까지의 소수를 구하는 문제다.
2 이상의 2의 배수는 배제할 수 있다.
유클리드 호제법과 n의 약수는 루트 n까지만 탐색하면 다 찾을 수 있다는 점을 이용해서 최적화가 가능하다.

```python
import sys


def is_prime(number):
    if number == 1:
        return False
    for divisor in range(2, int(number ** (1 / 2)) + 1):
        if number % divisor == 0:
            return False
    return True


while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    elif n == 1:
        total = 1
    else:
        total = 0
    start = n + 1 if n % 2 == 0 else n
    for num in range(start, 2 * n, 2):
        if is_prime(num):
            total += 1
    print(total)

```

소수를 찾는 연산을 여러번 하기 때문에 안되는 것 같다.
소수를 미리 찾거나, 이미 찾은 소수의 정보를 기억해야할 것 같다.
가장 작은 수와 가장 큰 수를 찾은 후에 가장 작은 수부터 가장 큰 수를 2 곱한 수의 범위의 소수를 전부 찾아서 리스트에 넣어준다.
그리고 소수 리스트에서 `n < prime <= 2*n`을 만족하는 범위에 있는 숫자들의 개수를 센다

```python
import sys


def is_prime(number):
    if number == 1:
        return False
    for divisor in range(2, int(number ** (1 / 2)) + 1):
        if number % divisor == 0:
            return False
    return True


numbers = []
while True:
    number = int(sys.stdin.readline())
    if number == 0:
        break
    numbers.append(number)
start = min(numbers)
primes = [2] if start == 2 else []
if start % 2 == 0:
    start += 1
end = max(numbers) * 2 + 1
for number in range(start, end):
    if is_prime(number):
        primes.append(number)

for number in numbers:
    length = len([prime for prime in primes if number < prime <= number * 2])
    print(length)

```

[1]: https://www.acmicpc.net/problem/4948

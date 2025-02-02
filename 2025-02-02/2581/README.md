# 2581

[코딩테스트 연습 - 2581][1] 로 이동

## 문제

자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최솟값을 찾는 프로그램을 작성하시오.
예를 들어 M=60, N=100인 경우 60이상 100이하의 자연수 중 소수는 61, 67, 71, 73, 79, 83, 89, 97 총 8개가 있으므로, 이들 소수의 합은 620이고, 최솟값은 61이 된다.

## 입력

입력의 첫째 줄에 M이, 둘째 줄에 N이 주어진다.
M과 N은 10,000이하의 자연수이며, M은 N보다 작거나 같다.

## 출력

M이상 N이하의 자연수 중 소수인 것을 모두 찾아 첫째 줄에 그 합을, 둘째 줄에 그 중 최솟값을 출력한다.
단, M이상 N이하의 자연수 중 소수가 없을 경우는 첫째 줄에 -1을 출력한다.

## 예제 입력

```
60
100

```

## 예제 출력

```
620
61

```

## 풀이

M부터 N까지의 소수를 전부 구하고 이들의 합과 가작 작은 소수를 구해야 한다.
약수의 개수가 2개이면 소수이다.
set 자료구조를 이용해서 중복된 약수를 없엘 수 있다.

```python
M = int(input())
N = int(input())
prime_numbers = []
for number in range(M, N + 1):
    divisors = {1, number}
    for divisor in range(2, number // 2 + 1):
        quotient, remains = divmod(number, divisor)
        if remains == 0:
            divisors.update([quotient, divisor])
    if len(divisors) == 2:
        prime_numbers.append(number)
if not prime_numbers:
    print(-1)
else:
    print(sum(prime_numbers), min(prime_numbers), sep="\n")

```

시간초과로 탈락했다.
sum과 min을 쓰지 않는 로직으로 바꿔보았다.

```python
M = int(input())
N = int(input())
min_prime = 0
sum_prime = 0
for number in range(M, N + 1):
    divisors = {1, number}
    for divisor in range(2, number // 2 + 1):
        quotient, remains = divmod(number, divisor)
        if remains == 0:
            divisors.update([quotient, divisor])
    if len(divisors) == 2:
        sum_prime += number
        if not min_prime:
            min_prime = number
if not sum_prime:
    print(-1)
else:
    print(sum_prime, min_prime, sep="\n")

```

또 시간초과로 탈락하였다.
만약 반복중에 나머지가 0이면 바로 소수가 아닌것으로 간주하여 반복을 종료하도록 하였다.

```python
M = int(input())
N = int(input())
prime_numbers = []
for number in range(M, N + 1):
    is_prime = True
    for divisor in range(2, number // 2 + 1):
        quotient, remains = divmod(number, divisor)
        if remains == 0:
            is_prime = False
            break
    if is_prime:
        prime_numbers.append(number)
if not prime_numbers:
    print(-1)
else:
    print(sum(prime_numbers), min(prime_numbers), sep="\n")

```

1은 소수가 아니므로 세지 않아야 한다.
M = max(2, M) 을 추가하여 M을 1부터 시작하지 않도록 한다.

```python
M = int(input())
N = int(input())
prime_numbers = []
M = max(2, M)
for number in range(M, N + 1):
    is_prime = True
    for divisor in range(2, number // 2 + 1):
        quotient, remains = divmod(number, divisor)
        if remains == 0:
            is_prime = False
            break
    if is_prime:
        prime_numbers.append(number)
if not prime_numbers:
    print(-1)
else:
    print(sum(prime_numbers), min(prime_numbers), sep="\n")

```

range 범위를 number의 제곱근 + 1로 줄였다.

```python
M = int(input())
N = int(input())
prime_numbers = []
M = max(2, M)
for number in range(M, N + 1):
    is_prime = True
    for divisor in range(2, int(number ** (1 / 2)) + 1):
        quotient, remains = divmod(number, divisor)
        if remains == 0:
            is_prime = False
            break
    if is_prime:
        prime_numbers.append(number)
if not prime_numbers:
    print(-1)
else:
    print(sum(prime_numbers), min(prime_numbers), sep="\n")

```

[1]: https://www.acmicpc.net/problem/2581

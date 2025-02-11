# 17103

[코딩테스트 연습 - 17103][1] 로 이동

## 문제

> 골드바흐의 추측: 2보다 큰 짝수는 두 소수의 합으로 나타낼 수 있다.

짝수 N을 두 소수의 합으로 나타내는 표현을 골드바흐 파티션이라고 한다. 짝수 N이 주어졌을 때, 골드바흐 파티션의 개수를 구해보자. 두 소수의 순서만 다른 것은 같은 파티션이다.

## 입력

첫째 줄에 테스트 케이스의 개수 T (1 ≤ T ≤ 100)가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 N은 짝수이고, 2 < N ≤ 1,000,000을 만족한다.

## 출력

각각의 테스트 케이스마다 골드바흐 파티션의 수를 출력한다.

## 예제 입력

```
5
6
8
10
12
100

```

## 예제 출력

```
1
1
2
1
6

```

## 풀이

에라토스테네스의 체 알고리즘은 2보다 큰 2의 배수는 소수 판별을 하지 않고,
3보다 큰 3의 배수는 소수 판별을 하지 않고,
5보다 큰 5의 배수는 ... 을 반복하는 알고리즘입니다.
소수를 먼저 구하고 소수의 배수는 배제하면 됩니다.

입력된 가장 큰 수를 구하고 그 수까지의 소수를 구한 다음, 입력된 수마다 가능한 조합의 개수를 찾으면 됩니다.

addend₀ 는 num의 2분의 1 지점까지 의 소수의 리스트고,
addend₁ 는 num의 2분의 1부터 num -1 까지의 소수의 리스트입니다.
addend₀ + addend₁ = num 인 가능한 모든 조합을 구하면 됩니다.

```python
import sys

primes = []
numbers = [int(num) for num in sys.stdin.read().split()[1:]]
end = max(numbers) + 1

for number in range(2, end):
    if all(number % prime != 0 for prime in primes):
        primes.append(number)

for number in numbers:
    addends1 = [prime for prime in primes if prime <= number // 2]
    addends2 = [prime for prime in primes if number // 2 <= prime < number]
    total = 0
    for addend1 in addends1:
        for addend2 in addends2:
            if addend1 + addend2 == number:
                total += 1
    print(total)

```

addend1과 2를 만들 필요 없이 number에서 addend를 뺐을때 소수면 둘 다 소수인것이다.

```python
import sys

N = int(sys.stdin.readline())
primes = []
numbers = []
for _ in range(N):
    number = int(sys.stdin.readline())
    numbers.append(number)
end = max(numbers) + 1

for number in range(2, end):
    if all(number % prime != 0 for prime in primes):
        primes.append(number)

for number in numbers:
    addends = [prime for prime in primes if prime <= number // 2]
    total = 0
    for addend in addends:
        if number - addend in primes:
            total += 1
    print(total)

```

시간 초과가 나온다.
이 코드는 primes가 많아질수록 연산을 점점 더 많이하여 오히려 느리다.
리스트의 인덱스를 이용한 알고리즘으로 변경하였다.

```python
import sys

N = int(sys.stdin.readline())
numbers = []
for _ in range(N):
    number = int(sys.stdin.readline())
    numbers.append(number)
end = max(numbers) + 1
primes = [True] * end
primes[0] = primes[1] = False

for index, value in enumerate(primes):
    if value:
        for composite in range(2 * index, end, index):
            primes[composite] = False

primes = [index for index, value in enumerate(primes) if value]

for number in numbers:
    addends = [prime for prime in primes if prime <= number // 2]
    total = 0
    for addend in addends:
        if number - addend in primes:
            total += 1
    print(total)

```

이것마저 시간 초과했습니다.

```python
import sys

N = int(sys.stdin.readline())
numbers = []
for _ in range(N):
    number = int(sys.stdin.readline())
    numbers.append(number)
end = max(numbers) + 1
primes = [True] * end
primes[0] = primes[1] = False

for index in range(2, int(end ** (0.5)) + 1):
    if primes[index]:
        for composite in range(2 * index, end, index):
            primes[composite] = False

primes = [index for index, value in enumerate(primes) if value]

for number in numbers:
    total = 0
    for prime in primes:
        if prime > number // 2:
            break
        if number - prime in primes:
            total += 1
    print(total)

```

에라토스테네스의 체 알고리즘을 루트 n까지만 반복하는것으로 최적화하고,
prime을 빼는 코드도 최적화했다.
그래도 느리다 프라임을 set 자료구조로 바꿔서 조회 성능을 상승시켯다.
하지만 입력마다 출력을 해줘야 한다.

```python
import sys

N = int(sys.stdin.readline())
for _ in range(N):
    number = int(sys.stdin.readline())
    primes = [True] * (number + 1)
    primes[0] = primes[1] = False
    for index in range(2, int(number ** (0.5)) + 1):
        if primes[index]:
            for composite in range(2 * index, number + 1, index):
                primes[composite] = False
    primes = set(index for index, value in enumerate(primes) if value)
    total = 0
    for prime in primes:
        if prime > number // 2:
            break
        if number - prime in primes:
            total += 1
    print(total)
```

처음부터 다시 작성해보겠습니다.

```python
import sys

numbers = [int(num) for num in sys.stdin.read().split()[1:]]
end = max(numbers) + 1
primes = [True] * end
primes[0] = primes[1] = False

for number in range(2, int(end**0.5) + 1):
    if primes[number]:
        for composite in range(2 * number, end, number):
            primes[composite] = False

primes = [index for index, value in enumerate(primes) if value]
prime_set = set(primes)

for number in numbers:
    total = 0
    for prime in primes:
        end = number // 2
        if prime > end:
            break
        if number - prime in prime_set:
            total += 1
    print(total)

```

각각의 단계마다 가장 최적화된 방법을 찾았더니 통과하였습니다.

[1]: https://www.acmicpc.net/problem/17103

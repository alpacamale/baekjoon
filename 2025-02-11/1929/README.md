# 1929

[코딩테스트 연습 - 1929][1] 로 이동

## 문제

M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

## 입력

첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.

## 출력

한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.

## 예제 입력

```
3 16

```

## 예제 출력

```
3
5
7
11
13

```

## 풀이

4134번과 로직은 비슷하다.

```python
primes = []

M, N = [int(num) for num in input().split()]


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


for number in range(M, N + 1):
    if is_prime(number):
        primes.append(number)

print(*primes, sep="\n")

```

[1]: https://www.acmicpc.net/problem/1929

# 1978

[코딩테스트 연습 - 1978][1] 로 이동

## 문제

주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

## 입력

첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

## 출력

주어진 수들 중 소수의 개수를 출력한다.

## 예제 입력

```
4
1 3 5 7

```

## 예제 출력

```
3

```

## 풀이

python에서 처음 input()은 쓸모없으므로 버린다.
숫자들을 numbers에 저장하고, 각각의 숫자가 소수인지 판별한다.
소수는 약수의 개수가 2개여야 한다.
set 자료구조를 이용해서 약수의 중복을 피한다.

```python
input()
numbers = [int(num) for num in input().split()]

result = 0
for number in numbers:
    divisors = {1, number}
    for divisor in range(2, number // 2 + 1):
        quotient, remains = divmod(number, divisor)
        if remains == 0:
            divisors.update([quotient, divisor])
    if len(divisors) == 2:
        result += 1
print(result)

```

range의 범위를 num의 제곱근 + 1 로 줄였다.

```python
input()
numbers = [int(num) for num in input().split()]

result = 0
for number in numbers:
    divisors = {1, number}
    for divisor in range(2, int(number ** (1 / 2) + 1)):
        quotient, remains = divmod(number, divisor)
        if remains == 0:
            divisors.update([quotient, divisor])
    if len(divisors) == 2:
        result += 1
print(result)

```

[1]: https://www.acmicpc.net/problem/1978

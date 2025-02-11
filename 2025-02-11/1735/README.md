# 1735

[코딩테스트 연습 - 1735][1] 로 이동

## 문제

분수 A/B는 분자가 A, 분모가 B인 분수를 의미한다. A와 B는 모두 자연수라고 하자.
두 분수의 합 또한 분수로 표현할 수 있다. 두 분수가 주어졌을 때, 그 합을 기약분수의 형태로 구하는 프로그램을 작성하시오. 기약분수란 더 이상 약분되지 않는 분수를 의미한다.

## 입력

첫째 줄과 둘째 줄에, 각 분수의 분자와 분모를 뜻하는 두 개의 자연수가 순서대로 주어진다. 입력되는 네 자연수는 모두 30,000 이하이다.

## 출력

첫째 줄에 구하고자 하는 기약분수의 분자와 분모를 뜻하는 두 개의 자연수를 빈 칸을 사이에 두고 순서대로 출력한다.

## 예제 입력

```
2 7

3 5


```

## 예제 출력

```
31 35


```

## 풀이

분모를 통분한 후에 더한 후 기약분수로 고치는 문제입니다.
더하는 두 분수가 둘 다 기약분수라면 더한 결과도 기약분수입니다.
문제에는 두 분수가 기약분수라는 조건이 없지만 있다고 가정하고 풀어보겠습니다.

```python
numer_a, denom_a = [int(num) for num in input().split()]
numer_b, denom_b = [int(num) for num in input().split()]
c = denom_a * denom_b
a, b = denom_a, denom_b
while b != 0:
    a, b = b, a % b

denom_c = c // a
numer_c = numer_a * (denom_c // denom_a) + numer_b * (denom_c // denom_b)
print(numer_c, denom_c)

```

두 수가 모두 기약분수라는 보장이 없는것 같습니다.
numer_c와 denom_c를 약분하는 코드를 추가합니다.

```python
numer_a, denom_a = [int(num) for num in input().split()]
numer_b, denom_b = [int(num) for num in input().split()]
c = denom_a * denom_b
a, b = denom_a, denom_b
while b != 0:
    a, b = b, a % b

denom_c = c // a
numer_c = numer_a * (denom_c // denom_a) + numer_b * (denom_c // denom_b)
a, b = numer_c, denom_c
while b != 0:
    a, b = b, a % b
print(numer_c // a, denom_c // a)

```

[1]: https://www.acmicpc.net/problem/1735

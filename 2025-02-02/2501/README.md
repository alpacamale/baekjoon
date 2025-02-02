# 2501

[코딩테스트 연습 - 2501][1] 로 이동

## 문제

어떤 자연수 p와 q가 있을 때, 만일 p를 q로 나누었을 때 나머지가 0이면 q는 p의 약수이다.
6을 예로 들면

- 6 ÷ 1 = 6 … 0
- 6 ÷ 2 = 3 … 0
- 6 ÷ 3 = 2 … 0
- 6 ÷ 4 = 1 … 2
- 6 ÷ 5 = 1 … 1
- 6 ÷ 6 = 1 … 0

그래서 6의 약수는 1, 2, 3, 6, 총 네 개이다.
두 개의 자연수 N과 K가 주어졌을 때, N의 약수들 중 K번째로 작은 수를 출력하는 프로그램을 작성하시오.

## 입력

첫째 줄에 N과 K가 빈칸을 사이에 두고 주어진다. N은 1 이상 10,000 이하이다. K는 1 이상 N 이하이다.

## 출력

첫째 줄에 N의 약수들 중 K번째로 작은 수를 출력한다. 만일 N의 약수의 개수가 K개보다 적어서 K번째 약수가 존재하지 않을 경우에는 0을 출력하시오.

## 예제 입력

```
6 3

```

## 예제 출력

```
3

```

## 풀이

약수는 1과 자기 자신을 반드시 포함한다.
약수는 대칭적으로 존재하기 때문에,
짝수 n의 약수는 1/2까지만 확인 14면 7까지만 확인한다.
홀수 n의 약수는 1/3까지만 확인 15면 5까지만 확인한다.
중복되는 약수의 제거는 if문을 사용하거나 set() 자료구조를 사용해야 한다.
이후 sort()를 이용해서 약수들을 정렬한 후 K - 1 번째 요소가 답이다.

```python
N, K = [int(num) for num in input().split()]
divisors = {1, N}
end = N // 2 + 1 if N % 2 == 0 else N // 3 + 1
for number in range(2, end):
    quotient, remains = divmod(N, number)
    if remains == 0:
        divisors.update([number, quotient])
if len(divisors) < K:
    print(0)
else:
    divisors = list(divisors)
    divisors.sort()
    print(divisors[K - 1])

```

range의 반복 범위를 N의 제곱근 + 1 까지로 줄였다.

```python
N, K = [int(num) for num in input().split()]
divisors = {1, N}
end = int(N ** (1 / 2)) + 1
for number in range(2, end):
    quotient, remains = divmod(N, number)
    if remains == 0:
        divisors.update([number, quotient])
if len(divisors) < K:
    print(0)
else:
    divisors = list(divisors)
    divisors.sort()
    print(divisors[K - 1])

```

[1]: https://www.acmicpc.net/problem/2501

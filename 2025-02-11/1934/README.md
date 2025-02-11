# 1934

[코딩테스트 연습 - 1934][1] 로 이동

## 문제

두 자연수 A와 B에 대해서, A의 배수이면서 B의 배수인 자연수를 A와 B의 공배수라고 한다. 이런 공배수 중에서 가장 작은 수를 최소공배수라고 한다. 예를 들어, 6과 15의 공배수는 30, 60, 90등이 있으며, 최소 공배수는 30이다.
두 자연수 A와 B가 주어졌을 때, A와 B의 최소공배수를 구하는 프로그램을 작성하시오.

## 입력

첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다. 둘째 줄부터 T개의 줄에 걸쳐서 A와 B가 주어진다. (1 ≤ A, B ≤ 45,000)

## 출력

첫째 줄부터 T개의 줄에 A와 B의 최소공배수를 입력받은 순서대로 한 줄에 하나씩 출력한다.

## 예제 입력

```
3
1 45000
6 10
13 17


```

## 예제 출력

```
45000
30
221


```

## 풀이

최소 공배수를 구하는법은 두 수를 소인수 분해한 뒤, 소인수 분해한 값들과 두 수의 나머지를 곱하면 된다.

```python
import sys

T = int(sys.stdin.readline())
for _ in range(T):
    quotients = []
    A, B = [int(num) for num in sys.stdin.readline().split()]
    divisor = 2
    bigger = max(A, B)
    while True:
        quotient_a, remain_a = divmod(A, divisor)
        quotient_b, remain_b = divmod(B, divisor)
        if remain_a == remain_b == 0:
            quotients.append(divisor)
            A = quotient_a
            B = quotient_b
            bigger = max(A, B)

        else:
            divisor += 1
            if bigger ** (1 / 2) < divisor:
                quotients.extend([A, B])
                break

    multiplyed = 1
    for number in quotients:
        multiplyed *= number
    print(multiplyed)

```

혹은 유클리드 호제법으로 최대공약수를 구하고, A X B // GCD를 하는 방법으로 구할 수 있다 (G X L == A X B)

```python
import sys

T = int(sys.stdin.readline())
for _ in range(T):
    A, B = [int(num) for num in sys.stdin.readline().split()]
    C = A * B
    while B != 0:
        A, B = B, A % B
    print(C // A)

```

[1]: https://www.acmicpc.net/problem/1934

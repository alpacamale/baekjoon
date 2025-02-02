# 9506

[코딩테스트 연습 - 9506][1] 로 이동

## 문제

어떤 숫자 n이 자신을 제외한 모든 약수들의 합과 같으면, 그 수를 완전수라고 한다.
예를 들어 6은 6 = 1 + 2 + 3 으로 완전수이다.
n이 완전수인지 아닌지 판단해주는 프로그램을 작성하라.

## 입력

입력은 테스트 케이스마다 한 줄 간격으로 n이 주어진다. (2 < n < 100,000)
입력의 마지막엔 -1이 주어진다.

## 출력

테스트케이스 마다 한줄에 하나씩 출력해야 한다.
n이 완전수라면, n을 n이 아닌 약수들의 합으로 나타내어 출력한다(예제 출력 참고).
이때, 약수들은 오름차순으로 나열해야 한다.
n이 완전수가 아니라면 n is NOT perfect. 를 출력한다.

## 예제 입력

```
6
12
28
-1

```

## 예제 출력

```
6 = 1 + 2 + 3
12 is NOT perfect.
28 = 1 + 2 + 4 + 7 + 14

```

## 풀이

약수는 1을 반드시 포함한다.
약수는 대칭적으로 존재하기 때문에,
짝수 n의 약수는 1/2까지만 확인 14면 7까지만 확인한다.
홀수 n의 약수는 1/3까지만 확인 15면 5까지만 확인한다.
중복되는 약수의 제거는 if문을 사용하거나 set() 자료구조를 사용해야 한다.

```python
import sys

while True:
    n = int(sys.stdin.readline())
    if n == -1:
        break
    divisors = {1}
    end = n // 2 + 1 if n % 2 == 0 else n // 3 + 1
    for num in range(2, end):
        quotient, remains = divmod(n, num)
        if remains == 0:
            divisors.update([quotient, num])
    message = (
        f"{n} is NOT perfect."
        if sum(divisors) != n
        else f"{n} = {" + ".join(str(num) for num in divisors)}"
    )
    print(message)

```

완전수를 출력할때 약수들이 정렬되지 않았다.

```python
import sys

while True:
    n = int(sys.stdin.readline())
    if n == -1:
        break
    divisors = {1}
    end = n // 2 + 1 if n % 2 == 0 else n // 3 + 1
    for num in range(2, end):
        quotient, remains = divmod(n, num)
        if remains == 0:
            divisors.update([quotient, num])
    message = (
        f"{n} is NOT perfect."
        if sum(divisors) != n
        else f"{n} = {" + ".join(str(num) for num in sorted(list(divisors)))}"
    )
    print(message)

```

end를 n의 제곱근 + 1로 설정하여 반복 횟수를 줄였다

```python
import sys

while True:
    n = int(sys.stdin.readline())
    if n == -1:
        break
    divisors = {1}
    end = int(n ** (1 / 2)) + 1
    for num in range(2, end):
        quotient, remains = divmod(n, num)
        if remains == 0:
            divisors.update([quotient, num])
    message = (
        f"{n} is NOT perfect."
        if sum(divisors) != n
        else f"{n} = {" + ".join(str(num) for num in sorted(list(divisors)))}"
    )
    print(message)

```

[1]: https://www.acmicpc.net/problem/9506

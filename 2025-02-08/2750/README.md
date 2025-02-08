# 2750

[코딩테스트 연습 - 2750][1] 로 이동

## 문제

N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

## 입력

첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 절댓값이 1,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

## 출력

첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

## 예제 입력

```
5
5
2
3
4
1

```

## 예제 출력

```
1
2
3
4
5

```

## 풀이

sort를 이용하면 쉽게 정렬할 수 있다.

```python
import sys

numbers = [int(number) for number in sys.stdin.read().split()]
for number in sorted(numbers):
    print(number)

```

첫줄에 N의 개수가 주어진다는 사실을 지금 알았다.
코드를 수정해준다

```python
import sys

numbers = [int(number) for number in sys.stdin.read().split()[1:]]
for number in sorted(numbers):
    print(number)

```

[1]: https://www.acmicpc.net/problem/2750

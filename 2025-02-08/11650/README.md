# 11650

[코딩테스트 연습 - 11650][1] 로 이동

## 문제

2차원 평면 위의 점 N개가 주어진다. 좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.

## 입력

첫째 줄에 점의 개수 N (1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N개의 줄에는 i번점의 위치 xi와 yi가 주어진다. (-100,000 ≤ xi, yi ≤ 100,000) 좌표는 항상 정수이고, 위치가 같은 두 점은 없다.

## 출력

첫째 줄부터 N개의 줄에 점을 정렬한 결과를 출력한다.

## 예제 입력

```
5
3 4
1 1
1 -1
2 2
3 3

```

## 예제 출력

```
1 -1
1 1
2 2
3 3
3 4

```

## 풀이

x좌표로 오름차순 정렬한 후에, y좌표로 오름차순한다.
sorted의 key에 튜플을 리턴하여 두가지 기준으로 정렬할 수 있다.

```python
import sys

N = int(sys.stdin.readline())
dots = []
for _ in range(N):
    dot = [int(num) for num in sys.stdin.readline().split()]
    dots.append(dot)
dots = sorted(dots, key=lambda x: (x[0], x[1]))
for x, y in dots:
    print(x, y)

```

내 코드에서는 잘 되지만 런타임 에러(NZEC)가 자꾸 나온다.s
stdin을 사용하지 않으니 잘 된다.
백준의 stdin 모듈이 뭔가 잘못된거같다.
rstrip을 해도 안된다.

```python
N = int(input())
dots = []
for _ in range(N):
    dot = [int(num) for num in input().split()]
    dots.append(dot)
dots = sorted(dots, key=lambda x: (x[0], x[1]))
for x, y in dots:
    print(x, y)

```

나중에 백준 사이트가 정상화되면 한번 더 제출해봐야겠다.

```python
import sys

N = int(sys.stdin.readline())
dots = [[int(num) for num in line.split()] for line in sys.stdin.read().split("\n")]
dots = sorted(dots, key=lambda x: (x[0], x[1]))
for x, y in dots:
    print(x, y)

```

[1]: https://www.acmicpc.net/problem/11650

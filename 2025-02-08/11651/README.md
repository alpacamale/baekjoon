# 11651

[코딩테스트 연습 - 11651][1] 로 이동

## 문제

2차원 평면 위의 점 N개가 주어진다. 좌표를 y좌표가 증가하는 순으로, y좌표가 같으면 x좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.

## 입력

첫째 줄에 점의 개수 N (1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N개의 줄에는 i번점의 위치 xi와 yi가 주어진다. (-100,000 ≤ xi, yi ≤ 100,000) 좌표는 항상 정수이고, 위치가 같은 두 점은 없다.

## 출력

첫째 줄부터 N개의 줄에 점을 정렬한 결과를 출력한다.

## 예제 입력

```
5
0 4
1 2
1 -1
2 2
3 3


```

## 예제 출력

```
1 -1
1 2
2 2
3 3
0 4


```

## 풀이

기본적으로 11650과 같은 문제입니다.
하지만 y좌표를 우선적으로 정렬하는 문제입니다.

```python
N = int(input())
dots = []
for _ in range(N):
    dot = [int(num) for num in input().split()]
    dots.append(dot)
dots = sorted(dots, key=lambda x: (x[1], x[0]))
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

[1]: https://www.acmicpc.net/problem/11651

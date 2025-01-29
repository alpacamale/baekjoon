# 2738

[코딩테스트 연습 - 2738][1] 로 이동

## 문제

N\*M크기의 두 행렬 A와 B가 주어졌을 때, 두 행렬을 더하는 프로그램을 작성하시오.

## 입력

첫째 줄에 행렬의 크기 N 과 M이 주어진다. 둘째 줄부터 N개의 줄에 행렬 A의 원소 M개가 차례대로 주어진다. 이어서 N개의 줄에 행렬 B의 원소 M개가 차례대로 주어진다. N과 M은 100보다 작거나 같고, 행렬의 원소는 절댓값이 100보다 작거나 같은 정수이다.

## 출력

첫째 줄부터 N개의 줄에 행렬 A와 B를 더한 행렬을 출력한다. 행렬의 각 원소는 공백으로 구분한다.

## 예제 입력

```
3 3
1 1 1
2 2 2
0 1 0
3 3 3
4 4 4
5 5 100
```

## 예제 출력

```
4 4 4
6 6 6
5 6 100
```

## 풀이

아래는 matrix1과 matrix2를 입력받아 생성하고,
matrix3에 더해주는 코드다.

```python
N, M = [int(num) for num in input().split()]
matrix1 = []
matrix2 = []
matrix3 = []

for row in range(N):
    cols = [int(num) for num in input().split()]
    matrix1.append(cols)

for row in range(N):
    cols = [int(num) for num in input().split()]
    matrix2.append(cols)

for row1, row2 in zip(matrix1, matrix2):
    row = []
    for col1, col2 in zip(row1, row2):
        col = str(col1 + col2)
        row.append(col)
    matrix3.append(row)

for row in matrix3:
    print(" ".join(row))

```

위의 코드는 불필요하게 matrix3를 생성하고,
컴프리헨션을 사용할 수 있는 코드를 for문을 사용하여 길게 나타내었다.
아래 코드는 위의 문제를 개선한것이다.

```python
N, M = [int(num) for num in input().split()]

matrix1 = [[int(num) for num in input().split()] for _ in range(N)]
matrix2 = [[int(num) for num in input().split()] for _ in range(N)]
for row1, row2 in zip(matrix1, matrix2):
    print(*[a + b for a, b in zip(row1, row2)])
```

[1]: https://www.acmicpc.net/problem/2738

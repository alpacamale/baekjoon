# 3009

[코딩테스트 연습 - 3009][1] 로 이동

## 문제

세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오.

## 입력

세 점의 좌표가 한 줄에 하나씩 주어진다. 좌표는 1보다 크거나 같고, 1000보다 작거나 같은 정수이다.

## 출력

직사각형의 네 번째 점의 좌표를 출력한다.

## 예제 입력

```
5 5
5 7
7 5

```

## 예제 출력

```
7 7

```

## 풀이

세 점의 x좌표 빈도수, y좌표 빈도수를 세서 빈도가 1인 숫자를 출력
혹은 세 점중 두 번 들어온 x좌표를 삭제해서 나머지 하나의 좌표를 출력

```python
x_coordinate = {}
y_coordinate = {}
for _ in range(3):
    x, y = [int(num) for num in input().split()]
    if x_coordinate.get(x, None):
        del x_coordinate[x]
    else:
        x_coordinate[x] = True
    if y_coordinate.get(y, None):
        del y_coordinate[y]
    else:
        y_coordinate[y] = True
print(list(x_coordinate.keys())[0], list(y_coordinate.keys())[0])

```

[1]: https://www.acmicpc.net/problem/3009

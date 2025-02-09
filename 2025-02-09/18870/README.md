# 18870

[코딩테스트 연습 - 18870][1] 로 이동

## 문제

수직선 위에 N개의 좌표 X1, X2, ..., XN이 있다. 이 좌표에 좌표 압축을 적용하려고 한다.
Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표 Xj의 개수와 같아야 한다.
X1, X2, ..., XN에 좌표 압축을 적용한 결과 X'1, X'2, ..., X'N를 출력해보자.

## 입력

첫째 줄에 N이 주어진다.
둘째 줄에는 공백 한 칸으로 구분된 X1, X2, ..., XN이 주어진다.

## 출력

첫째 줄에 X'1, X'2, ..., X'N을 공백 한 칸으로 구분해서 출력한다.

## 예제 입력

```
5
2 4 -10 4 -9

```

## 예제 출력

```
2 3 0 3 1

```

## 풀이

가장 작은 좌표를 0이라고 하고, 그로부터 숫자가 커지면 0이라고 하는 것 같다.
딕셔너리로 숫자와 숫자를 오름차순했을때 순서(인덱스)를 매핑하고,
for문으로 딕셔너리의 키에 number를 순서대로 전달해주면 완성이다.

```python
N = int(input())
numbers = [int(num) for num in input().split()]
number_sets = set(numbers)
ordered = {number: index for index, number in enumerate(sorted(list(number_sets)))}
result = [ordered[number] for number in numbers]
print(*result, sep=" ")

```

최적화를 노리기 위해 number_sets변수를 사용하지 않았는데, 결과는 20ms 빨라진것으로 거의 차이가 없었습니다.

```python
N = int(input())
numbers = [int(num) for num in input().split()]
ordered = {number: index for index, number in enumerate(sorted(list(set(numbers))))}
result = [ordered[number] for number in numbers]
print(*result, sep=" ")

```

[1]: https://www.acmicpc.net/problem/18870

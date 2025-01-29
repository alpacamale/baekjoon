# 1330

[코딩테스트 연습 - 1330][1] 로 이동

## 문제

두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하시오.

## 입력

첫째 줄에 A와 B가 주어진다. A와 B는 공백 한 칸으로 구분되어져 있다.

## 출력

첫째 줄에 다음 세 가지 중 하나를 출력한다.

## 예제 입력

```
1 2
```

## 예제 출력

```
<
```

## 풀이

조건문을 이용해서 조건에 맞는 작업을 처리해 줄 수 있다.

```python
A, B = [int(char) for char in input().split()]
if A > B:
    print(">")
elif A < B:
    print("<")
else:
    print("==")

```

[1]: https://www.acmicpc.net/problem/1330

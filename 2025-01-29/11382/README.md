# 11382

[코딩테스트 연습 - 11382][1] 로 이동

## 문제

꼬마 정민이는 이제 A + B 정도는 쉽게 계산할 수 있다. 이제 A + B + C를 계산할 차례이다!

## 입력

첫 번째 줄에 A, B, C (1 ≤ A, B, C ≤ 1012)이 공백을 사이에 두고 주어진다.

## 출력

A+B+C의 값을 출력한다.

## 예제 입력

```
77 77 7777
```

## 예제 출력

```
7931
```

## 풀이

A, B에 나누어 담던것을 A, B, C 로 담아주면 된다.

```python
A, B, C = [int(char) for char in input().split()]
print(A + B + C)

```

[1]: https://www.acmicpc.net/problem/11382

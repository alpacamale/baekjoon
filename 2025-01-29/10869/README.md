# 10869

[코딩테스트 연습 - 10869][1] 로 이동

## 문제

두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A\*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오.

## 입력

두 자연수 A와 B가 주어진다. (1 ≤ A, B ≤ 10,000)

## 출력

첫째 줄에 A+B, 둘째 줄에 A-B, 셋째 줄에 A\*B, 넷째 줄에 A/B, 다섯째 줄에 A%B를 출력한다.

## 예제 입력

```
7 3
```

## 예제 출력

```
10

4

21

2

1
```

## 풀이

입력받은 A와 B를 공백을 기준으로 분리하기 위해서 input과 split을 사용하고,
각각의 연산 결과를 print로 출력해주면 된다.

```python
A, B = [int(char) for char in input().split()]
print(A + B)
print(A - B)
print(A * B)
print(A // B)
print(A % B)

```

[1]: https://www.acmicpc.net/problem/10869

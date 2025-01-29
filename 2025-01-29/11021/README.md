# 11021

[코딩테스트 연습 - 11021][1] 로 이동

## 문제

두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

## 입력

첫째 줄에 테스트 케이스의 개수 T가 주어진다.

## 출력

각 테스트 케이스마다 "Case #x: "를 출력한 다음, A+B를 출력한다. 테스트 케이스 번호는 1부터 시작한다.

## 예제 입력

```
5
1 1
2 3
3 4
9 8
5 2
```

## 예제 출력

```
Case #1: 2
Case #2: 5
Case #3: 7
Case #4: 17
Case #5: 7
```

## 풀이

A + B 문제에서 문제의 case를 출력하는것이 추가되었다.
for문과 range를 이용해서 인덱싱해주면 된다.

```python
T = int(input())

for t in range(1, T + 1):
    A, B = [int(num) for num in input().split()]
    print(f"Case #{t}: {A + B}")

```

[1]: https://www.acmicpc.net/problem/11021

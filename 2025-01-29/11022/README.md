# 11022

[코딩테스트 연습 - 11022][1] 로 이동

## 문제

두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

## 입력

첫째 줄에 테스트 케이스의 개수 T가 주어진다.

## 출력

각 테스트 케이스마다 "Case #x: A + B = C" 형식으로 출력한다. x는 테스트 케이스 번호이고 1부터 시작하며, C는 A+B이다.

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
Case #1: 1 + 1 = 2
Case #2: 2 + 3 = 5
Case #3: 3 + 4 = 7
Case #4: 9 + 8 = 17
Case #5: 5 + 2 = 7
```

## 풀이

f 스트링을 이용해서 편하게 출력할 수 있다.

```python
T = int(input())

for t in range(1, T + 1):
    A, B = [int(num) for num in input().split()]
    print(f"Case #{t}: {A} + {B} = {A + B}")

```

[1]: https://www.acmicpc.net/problem/11022

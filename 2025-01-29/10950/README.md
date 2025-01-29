# 10950

[코딩테스트 연습 - 10950][1] 로 이동

## 문제

두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

## 입력

첫째 줄에 테스트 케이스의 개수 T가 주어진다.

## 출력

각 테스트 케이스마다 A+B를 출력한다.

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
2
5
7
17
7
```

## 풀이

for 문을 이용해서 입력과 출력을 반복해주었다.

```python
times = int(input())

for time in range(times):
    A, B = [int(num) for num in input().split()]
    print(A + B)

```

[1]: https://www.acmicpc.net/problem/10950

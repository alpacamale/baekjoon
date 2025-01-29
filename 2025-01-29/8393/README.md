# 8393

[코딩테스트 연습 - 8393][1] 로 이동

## 문제

n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.

## 입력

첫째 줄에 n (1 ≤ n ≤ 10,000)이 주어진다.

## 출력

1부터 n까지 합을 출력한다.

## 예제 입력

```
3
```

## 예제 출력

```
6
```

## 풀이

sum과 제너레이터 컴프리헨션을 이용해서 풀 수 있다.

```python
n = int(input())
total = sum(num for num in range(1, n + 1))
print(total)

```

[1]: https://www.acmicpc.net/problem/8393

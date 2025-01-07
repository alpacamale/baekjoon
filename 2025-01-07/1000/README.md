# 1000

[코딩테스트 연습 - 1000][1] 로 이동

## 문제

두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

## 입력

첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)

## 출력

첫째 줄에 A+B를 출력한다.

## 예제 입력

```
1 2
```

## 예제 출력

```
3
```

## 풀이

파이썬 내장함수 sum()을 이용해서 입력받은 숫자의 합을 구하고, 출력해주었다.
```python
result = sum(int(number) for number in input().split())
print(result)
```

[1]: https://www.acmicpc.net/problem/1000

# 2588

[코딩테스트 연습 - 2588][1] 로 이동

## 문제

(세 자리 수) × (세 자리 수)는 다음과 같은 과정을 통하여 이루어진다.

## 입력

첫째 줄에 (1)의 위치에 들어갈 세 자리 자연수가, 둘째 줄에 (2)의 위치에 들어갈 세자리 자연수가 주어진다.

## 출력

첫째 줄부터 넷째 줄까지 차례대로 (3), (4), (5), (6)에 들어갈 값을 출력한다.

## 예제 입력

```
472
385
```

## 예제 출력

```
2360
3776
1416
181720
```

## 풀이

각 자리수를 정수 형태로 A, B, C 에 저장하고,
C, B, A 순서로 곱한 숫자를 출력해준다.

```python
number = int(input())
number2 = input()
A, B, C = [int(char) for char in number2]
print(number * C)
print(number * B)
print(number * A)
print(number * int(number2))

```

[1]: https://www.acmicpc.net/problem/2588

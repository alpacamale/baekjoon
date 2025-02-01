# 11005

[코딩테스트 연습 - 11005][1] 로 이동

## 문제

10진법 수 N이 주어진다. 이 수를 B진법으로 바꿔 출력하는 프로그램을 작성하시오.
10진법을 넘어가는 진법은 숫자로 표시할 수 없는 자리가 있다. 이런 경우에는 다음과 같이 알파벳 대문자를 사용한다.
A: 10, B: 11, ..., F: 15, ..., Y: 34, Z: 35

## 입력

첫째 줄에 N과 B가 주어진다. (2 ≤ B ≤ 36) N은 10억보다 작거나 같은 자연수이다.

## 출력

첫째 줄에 10진법 수 N을 B진법으로 출력한다.

## 예제 입력

```
60466175 36

```

## 예제 출력

```
ZZZZZ

```

## 풀이

10진법을 n진법으로 변환하는 방법은 숫자를 n으로 계속 나누면서 n으로 나눈 나머지를 기록한 후에, 기록한 나머지를 역순으로 배열하면 n진법이 된다.
divmod() 함수는 나눗셈의 몫과 나머지를 반환하는 함수다.

```python
N, B = [int(num) for num in input().split()]

remainders = []
while N != 0:
    N, mod = divmod(N, B)
    remainders.append(mod)

numeral = (
    "".join(chr(num + 55) if num >= 10 else str(num) for num in remainders[::-1]) or "0"
)
print(numeral)

```

[1]: https://www.acmicpc.net/problem/11005

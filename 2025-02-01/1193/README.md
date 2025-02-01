# 1193

[코딩테스트 연습 - 1193][1] 로 이동

## 문제

무한히 큰 배열에 다음과 같이 분수들이 적혀있다.

|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |
| 1/1 | 1/2 | 1/3 | 1/4 | 1/5 | …   |
| 2/1 | 2/2 | 2/3 | 2/4 | …   | …   |
| 3/1 | 3/2 | 3/3 | …   | …   | …   |
| 4/1 | 4/2 | …   | …   | …   | …   |
| 5/1 | …   | …   | …   | …   | …   |
| …   | …   | …   | …   | …   | …   |

이와 같이 나열된 분수들을 1/1 → 1/2 → 2/1 → 3/1 → 2/2 → … 과 같은 지그재그 순서로 차례대로 1번, 2번, 3번, 4번, 5번, … 분수라고 하자.
X가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성하시오.

## 입력

첫째 줄에 X(1 ≤ X ≤ 10,000,000)가 주어진다.

## 출력

첫째 줄에 분수를 출력한다.

## 예제 입력

```
1

```

## 예제 출력

```
1/1

```

## 풀이

대각선끼리 분모와 분자의 총합은 같고, 지그재그로 움직입니다.
flag로 방향을 설정하고 True일경우 분모가 증가, False일경우 분자가 증가합니다.
대각선 내에서 숫자가 더 증가할 수 없다면 다음 대각선으로 이동하고, 방향을 바꿉니다.

```python
numerator = 1
denominator = 1
flag = True
num = 1
X = int(input())

for _ in range(X - 1):
    if (not flag and num == numerator) or (flag and num == denominator):
        if flag:
            denominator += 1
        else:
            numerator += 1
        flag = not flag
        num += 1
    elif flag:
        denominator += 1
        numerator -= 1
    elif not flag:
        denominator -= 1
        numerator += 1


print(f"{numerator}/{denominator}")

```

위의 코드는 답은 나오지만 시간이 초과합니다.
반복을 줄이면서 답을 구하는 알고리즘을 찾아야 합니다.
분모와 분자의 합을 total이라고 할 때, x와 total의 관계는 다음과 같습니다.

X 1 -> total 2
X 2 -> total 3
X 4 -> total 4
X 7 -> total 5
X 11 -> total 6
X 16 -> total 7

X가 2일 때를 제외하면, X < 0 + 1 + 2 ... + total - 1을 만족합니다.

그리고 total이 짝수일때는 X가 증가할수록 분모가 커지고,
홀수일때는 X가 증가할수록 분자가 커집니다.
분모와 분자의 최대 크기는 total - 1 입니다.

따라서 코드는 아래와 같습니다.

```python
X = int(input())
num = 2
while X > sum(range(num)):
    num += 1

number1 = num - X + sum(range(num - 1))
number2 = num - number1
if num % 2 == 0:
    print(number1, number2, sep="/")
else:
    print(number2, number1, sep="/")

```

삼각수의 성질을 이용해서 sum(range())를 연산 횟수가 적은 곱셈식으로 나타낼 수 있습니다.

```python
X = int(input())
total = 2
while X > total * (total - 1) // 2:
    total += 1

number1 = total - X + (total - 1) * (total - 2) // 2
number2 = total - number1
if total % 2 == 0:
    print(number1, number2, sep="/")
else:
    print(number2, number1, sep="/")

```

[1]: https://www.acmicpc.net/problem/1193

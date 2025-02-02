# 5086

[코딩테스트 연습 - 5086][1] 로 이동

## 문제

4 × 3 = 12이다.
이 식을 통해 다음과 같은 사실을 알 수 있다.
3은 12의 약수이고, 12는 3의 배수이다.
4도 12의 약수이고, 12는 4의 배수이다.
두 수가 주어졌을 때, 다음 3가지 중 어떤 관계인지 구하는 프로그램을 작성하시오.
첫 번째 숫자가 두 번째 숫자의 약수이다.
첫 번째 숫자가 두 번째 숫자의 배수이다.
첫 번째 숫자가 두 번째 숫자의 약수와 배수 모두 아니다.

## 입력

입력은 여러 테스트 케이스로 이루어져 있다. 각 테스트 케이스는 10,000이 넘지않는 두 자연수로 이루어져 있다. 마지막 줄에는 0이 2개 주어진다. 두 수가 같은 경우는 없다.

## 출력

각 테스트 케이스마다 첫 번째 숫자가 두 번째 숫자의 약수라면 factor를, 배수라면 multiple을, 둘 다 아니라면 neither를 출력한다.

## 예제 입력

```
8 16
32 4
17 5
0 0


```

## 예제 출력

```
factor
multiple
neither


```

## 풀이

```python
import sys

for line in sys.stdin.readlines():
    number1, number2 = [int(num) for num in line.split()]
    print(number1, number2)
    if number1 == number2 == 0:
        sys.exit(0)
    elif number2 % number1 == 0:
        print("factor")
    elif number1 % number2 == 0:
        print("multiple")
    else:
        print("neither")

```

백준 코드 입력에 EOD가 없는것같다.

for문이 아닌 while문과 readline()을 사용하여 문자열을 받는다.

```python
import sys

while True:
    number1, number2 = [int(num) for num in sys.stdin.readline().split()]
    if number1 == number2 == 0:
        break
    elif number2 % number1 == 0:
        print("factor")
    elif number1 % number2 == 0:
        print("multiple")
    else:
        print("neither")

```

[1]: https://www.acmicpc.net/problem/5086

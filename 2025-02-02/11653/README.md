# 11653

[코딩테스트 연습 - 11653][1] 로 이동

## 문제

정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.

## 입력

첫째 줄에 정수 N (1 ≤ N ≤ 10,000,000)이 주어진다.

## 출력

N의 소인수분해 결과를 한 줄에 하나씩 오름차순으로 출력한다. N이 1인 경우 아무것도 출력하지 않는다.

## 예제 입력

```
72

```

## 예제 출력

```
2
2
2
3
3

```

## 풀이

만약 나누었을때 나머지가 0이라면, 약수이므로 print로 출력해주고,
그렇지 않은 경우 더 큰 숫자로 나누어본다.
이렇게 나누다보면 N이 1이 되는 순간이 오는데, 그렇다면 소인수분해가 끝난것이다.

```python
N = int(input())

divisor = 2
while N != 1:
    quotient, remains = divmod(N, divisor)
    if remains == 0:
        print(divisor)
        N = quotient
    else:
        divisor += 1

```

속도가 느려서 반복을 N // 2 까지만 하게 하였다.
만약 N이 아주 큰 소수일경우 코드가 빨라진다.

```python
N = int(input())

divisor = 2
end = N // 2 + 1
while N != 1:
    quotient, remains = divmod(N, divisor)
    if remains == 0:
        print(divisor)
        N = quotient
    else:
        if divisor == end:
            print(N)
            break
        divisor += 1

```

위의 코드도 느려서 N이 초기화 될때마다 end도 다시 계산하도록 하였다.
이제 인수분해할때 마지막으로 나누는 수가 아주 큰 소수더라도 빨리 계산할 수 있다.

```python
N = int(input())

divisor = 2
end = N // 2 + 1
while N != 1:
    quotient, remains = divmod(N, divisor)
    if remains == 0:
        print(divisor)
        N = quotient
        end = N // 2 + 1
    else:
        if divisor == end:
            print(N)
            break
        divisor += 1

```

소수의 계산 횟수를 더 최적화 하기 위해서 end를 N의 제곱근 + 1까지로 설정해주었다.

```python
N = int(input())

divisor = 2
end = int(N ** (1 / 2)) + 1
while N != 1:
    quotient, remains = divmod(N, divisor)
    if remains == 0:
        print(divisor)
        N = quotient
        end = int(N ** (1 / 2)) + 1
    else:
        if divisor == end:
            print(N)
            break
        divisor += 1
```

[1]: https://www.acmicpc.net/problem/11653

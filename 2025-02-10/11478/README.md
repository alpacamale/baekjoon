# 11478

[코딩테스트 연습 - 11478][1] 로 이동

## 문제

문자열 S가 주어졌을 때, S의 서로 다른 부분 문자열의 개수를 구하는 프로그램을 작성하시오.
부분 문자열은 S에서 연속된 일부분을 말하며, 길이가 1보다 크거나 같아야 한다.
예를 들어, ababc의 부분 문자열은 a, b, a, b, c, ab, ba, ab, bc, aba, bab, abc, abab, babc, ababc가 있고, 서로 다른것의 개수는 12개이다.

## 입력

첫째 줄에 문자열 S가 주어진다. S는 알파벳 소문자로만 이루어져 있고, 길이는 1,000 이하이다.

## 출력

첫째 줄에 S의 서로 다른 부분 문자열의 개수를 출력한다.

## 예제 입력

```
ababc


```

## 예제 출력

```
12


```

## 풀이

모든 중복되지 않은 부분 문자열을 구하고 그 개수를 구해야 한다.
set 자료구조를 사용하면 편하다.

```python
S = input()
length = len(S)
substrings = set()
for number in range(length):
    start = 0
    end = start + number + 1
    while end <= length:
        substrings.add(S[start:end])
        start += 1
        end = start + number + 1
print(len(substrings))

```

[1]: https://www.acmicpc.net/problem/11478

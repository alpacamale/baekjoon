# 14425

[코딩테스트 연습 - 14425][1] 로 이동

## 문제

총 N개의 문자열로 이루어진 집합 S가 주어진다.
입력으로 주어지는 M개의 문자열 중에서 집합 S에 포함되어 있는 것이 총 몇 개인지 구하는 프로그램을 작성하시오.

## 입력

첫째 줄에 문자열의 개수 N과 M (1 ≤ N ≤ 10,000, 1 ≤ M ≤ 10,000)이 주어진다.
다음 N개의 줄에는 집합 S에 포함되어 있는 문자열들이 주어진다.
다음 M개의 줄에는 검사해야 하는 문자열들이 주어진다.
입력으로 주어지는 문자열은 알파벳 소문자로만 이루어져 있으며, 길이는 500을 넘지 않는다. 집합 S에 같은 문자열이 여러 번 주어지는 경우는 없다.

## 출력

첫째 줄에 M개의 문자열 중에 총 몇 개가 집합 S에 포함되어 있는지 출력한다.

## 예제 입력

```
5 11
baekjoononlinejudge
startlink
codeplus
sundaycoding
codingsh
baekjoon
codeplus
codeminus
startlink
starlink
sundaycoding
codingsh
codinghs
sondaycoding
startrink
icerink

```

## 예제 출력

```
4

```

## 풀이

python in 을 사용하여 word_set 안에 word가 있는지 확인한다.

```python
import sys

N, M = [int(num) for num in input().split()]

word_set = set()
for _ in range(N):
    word_set.add(sys.stdin.readline().rstrip())
words = [word.rstrip() for word in sys.stdin.readlines()]
print(sum(1 for word in words if word in word_set))

```

[1]: https://www.acmicpc.net/problem/14425

# 1157

[코딩테스트 연습 - 1157][1] 로 이동

## 문제

알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.

## 입력

첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

## 출력

첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

## 예제 입력

```
Mississipi
```

## 예제 출력

```
?
```

## 풀이

시간초과로 실패한 코드
string.count 부분이 문제인것으로 보인다.

```python
string = input().upper()
string_counts = {char: string.count(char) for char in string}
max_count = max(string_counts.values())
if list(string_counts.values()).count(max_count) != 1:
    print("?")
else:
    print(max(string_counts, key=lambda x: string_counts[x]))

```

```python
string = input().upper()
string_counts = {}
for char in string:
    if string_counts.get(char, None):
        string_counts[char] += 1
    else:
        string_counts[char] = 1

max_count = max(string_counts.values())
if list(string_counts.values()).count(max_count) != 1:
    print("?")
else:
    print(max(string_counts, key=lambda x: string_counts[x]))

```

[1]: https://www.acmicpc.net/problem/1157

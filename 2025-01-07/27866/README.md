# 27866

[코딩테스트 연습 - 27866][1] 로 이동

## 문제

단어 $S$와 정수 $i$가 주어졌을 때, $S$의 $i$번째 글자를 출력하는 프로그램을 작성하시오.

## 입력

첫째 줄에 영어 소문자와 대문자로만 이루어진 단어 $S$가 주어진다. 단어의 길이는 최대 $1\,000$이다.

둘째 줄에 정수 $i$가 주어진다. ($1 \le i \le \left|S\right|$)

## 출력

$S$의 $i$번째 글자를 출력한다.

## 예제 입력

```
Sprout
3
```

## 예제 출력

```
r
```

## 풀이

string의 i -1 번째 인덱스의 char를 출력해주면 된다.

```python
string = input()
index = int(input()) - 1

print(string[index])
```

[1]: https://www.acmicpc.net/problem/27866

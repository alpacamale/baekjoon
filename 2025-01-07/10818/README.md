# 10818

[코딩테스트 연습 - 10818][1] 로 이동

## 문제

N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.

## 입력

첫째 줄에 정수의 개수 N (1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄에는 N개의 정수를 공백으로 구분해서 주어진다. 모든 정수는 -1,000,000보다 크거나 같고, 1,000,000보다 작거나 같은 정수이다.

## 출력

첫째 줄에 주어진 정수 N개의 최솟값과 최댓값을 공백으로 구분해 출력한다.

## 예제 입력

```
5
20 10 35 30 7
```

## 예제 출력

```
7 35
```

## 풀이

min() 함수와 max() 함수를 이용해서 풀 수 있다.

```python
length = input()
numbers = (int(x) for x in input().split())
min_number = min(numbers)
max_number = max(numbers)

print(min_number, max_number)
```

만약 length의 길이가 길어지면 리스트를 한번만 반복 하도록 코드를 수정할 수 있있다.
inf 를 사용해서 값을 초기화 시켜줄 수 있다.

```python
length = input()
numbers = (int(x) for x in input().split())
min_number = float("inf")
max_number = float("-inf")

for number in numbers:
    min_number = min(min_number, number)
    max_number = max(max_number, number)

print(min_number, max_number)
```

[1]: https://www.acmicpc.net/problem/10818

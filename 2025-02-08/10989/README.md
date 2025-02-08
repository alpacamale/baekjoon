# 10989

[코딩테스트 연습 - 10989][1] 로 이동

## 문제

N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

## 입력

첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.

## 출력

첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

## 예제 입력

```
10
5
2
3
1
4
2
3
5
1
7

```

## 예제 출력

```
1
1
2
2
3
3
4
5
5
7

```

## 풀이

2751번의 코드와 동일하게 해봤습니다.

```python
import sys

numbers = [int(num) for num in sys.stdin.read().split()[1:]]
print(*sorted(numbers), sep="\n")

```

메모리 초과로 실패가 나왔습니다. N의 값이 10배 커져서 그런거같습니.
stdin.read()로 한번에 읽지 않고 stdin.readlines()로 읽어야겠습니다.
메모리를 덜 사용하게 끔 언팩도 안하고 sorted보다 sort를 사용했습니다.

```python
import sys

N = int(sys.stdin.readline())
numbers = []
for num in range(N):
    numbers.append(int(sys.stdin.readline()))
numbers.sort()
for num in numbers:
    print(num)

```

이래도 메모리 초과가 나옵니다.
메모리를 적게 쓰는 버블 정렬 알고리즘을 직접 정의하여 문제를 풀어야겠습니다.

```python
import sys


def bubble_sort(array):
    length = len(array)
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for index in range(length - 1):
            if array[index] > array[index + 1]:
                array[index], array[index + 1] = array[index + 1], array[index]
                is_sorted = False
    return array


N = int(sys.stdin.readline())
numbers = []
for num in range(N):
    numbers.append(int(sys.stdin.readline()))
numbers = bubble_sort(numbers)
for num in numbers:
    print(num)

```

이래도 메모리 초과가 나옵니다.
파이썬의 heapq 모듈을 사용합니다.

```python
import sys
import heapq


N = int(sys.stdin.readline())
heap = []

for _ in range(N):
    heapq.heappush(heap, int(sys.stdin.readline()))

while heap:
    print(heapq.heappop(heap))

```

이것도 메모리 초과가 나왔습니다.
메모리를 너무 적게준게 아닌가 싶지만 이래도 통과하는사람은 통과합니다.
애초에 새로 정렬한 array를 다시 array에 대입하는 과정에서 엄청난 메모리가 낭비됩니다.
카운팅 정렬이라는게 있다고 합니다.
한정적인 숫자가 인풋으로 들어오기 때문에 counter에 숫자가 몇번씩 나왔는지 저장하고, counter의 value만큼 숫자를 출력하는것입니다.

```python
import sys

N = int(sys.stdin.readline())
counter = {}

for _ in range(N):
    number = int(sys.stdin.readline())
    if counter.get(number):
        counter[number] += 1
    else:
        counter[number] = 1

keys = sorted(counter.keys())
for key in keys:
    numbers = [key] * counter[key]
    print(*numbers, sep="\n")

```

이것도 메모리 초과가 나왔습니다.
print 할때 numbers를 언팩하지않고 이것도 for문으로 출력해야겠습니다.

```python
import sys

N = int(sys.stdin.readline())
counter = {}

for _ in range(N):
    number = int(sys.stdin.readline())
    if counter.get(number):
        counter[number] += 1
    else:
        counter[number] = 1

keys = sorted(counter.keys())
for key in keys:
    for _ in range(counter[key]):
        print(key)

```

드디어 통과했습니다.
하지만 코드가 느립니다.
N이 엄청 커다란 수인데 range를 사용하면 메모리를 많이 쓸것같습니다.
for문 대신 while문을 써줍니다.

```python
import sys

N = int(sys.stdin.readline())
counter = {}

while True:
    number = sys.stdin.readline()
    if not number:
        break
    number = int(number)
    if counter.get(number):
        counter[number] += 1
    else:
        counter[number] = 1

keys = sorted(counter.keys())
for key in keys:
    for _ in range(counter[key]):
        print(key)

```

while문으로 메모리를 한번 최적화 했습니다.
range가 차지하던 메모리는 N _ pyton int가 차지하는 byte였습니다.
그만큼의 메모리 여유가 생겼기 때문에,
출력하는 코드에서 이중 for문을 사용하지 않고 언팩을 사용하는 메모리 여유가 생겼다고 할 수 있습니다.
언팩한 메모리의 길이는 [counter[key] _ python int] \* 2 라고 할 수있습니다.(리스트 만들때 길이 + 리스트 언팩한 길이)
최악의 경우 메모리때문에 탈락할 수 있지만 한번 시도해 보겠습니다.

```python
import sys

N = int(sys.stdin.readline())
counter = {}

while True:
    number = sys.stdin.readline()
    if not number:
        break
    number = int(number)
    if counter.get(number):
        counter[number] += 1
    else:
        counter[number] = 1

keys = sorted(counter.keys())
for key in keys:
    numbers = [key] * counter[key]
    print(*numbers, sep="\n")

```

메모리 초과가 나왔습니다.
문제 예시중에 한가지 숫자만 여러번 나오는 예시가 있는것 같습니다.
딕셔너리는 해시테이블을 사용하기 때문에 메모리 효율이 안좋을 수 있습니다.
리스트는 연속된 배열을 사용하기때문에 오버헤드가 없고 메모리 효율이 좋습니다.
counter 딕셔너리가 아닌 리스트를 사용해서 문제를 풀어보겠습니다.

```python
import sys

N = int(sys.stdin.readline())
counts = [0] * 10001

while True:
    number = sys.stdin.readline()
    if not number:
        break
    counts[int(number)] += 1

for index, count in enumerate(counts):
    numbers = [index] * count
    if numbers:
        print(*numbers, sep="\n")

```

위의 코드도 메모리 초과가 나왔기때문에,
언팩하는 방법은 포기하고 하겠습니다.

```python
import sys

N = int(sys.stdin.readline())
counts = [0] * 10001

while True:
    number = sys.stdin.readline()
    if not number:
        break
    counts[int(number)] += 1

for index, count in enumerate(counts):
    for _ in range(count):
        print(index)

```

이 코드가 최종 코드입니다.

[1]: https://www.acmicpc.net/problem/10989

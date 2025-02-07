# 1018

[코딩테스트 연습 - 1018][1] 로 이동

## 문제

지민이는 자신의 저택에서 MN개의 단위 정사각형으로 나누어져 있는 M×N 크기의 보드를 찾았다. 어떤 정사각형은 검은색으로 칠해져 있고, 나머지는 흰색으로 칠해져 있다. 지민이는 이 보드를 잘라서 8×8 크기의 체스판으로 만들려고 한다.
체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 한다. 구체적으로, 각 칸이 검은색과 흰색 중 하나로 색칠되어 있고, 변을 공유하는 두 개의 사각형은 다른 색으로 칠해져 있어야 한다. 따라서 이 정의를 따르면 체스판을 색칠하는 경우는 두 가지뿐이다. 하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우이다.
보드가 체스판처럼 칠해져 있다는 보장이 없어서, 지민이는 8×8 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다고 생각했다. 당연히 8\*8 크기는 아무데서나 골라도 된다. 지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.

## 입력

첫째 줄에 N과 M이 주어진다. N과 M은 8보다 크거나 같고, 50보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에는 보드의 각 행의 상태가 주어진다. B는 검은색이며, W는 흰색이다.

## 출력

첫째 줄에 지민이가 다시 칠해야 하는 정사각형 개수의 최솟값을 출력한다.

## 예제 입력

```
8 8
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBBBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW

```

## 예제 출력

```
1

```

## 풀이

이중 for문을 이용해서 자를 수 있는 범위의 체스판을 모두 확인한 다음, 각각의 칠해야 하는 개수를 구한 뒤, 가장 작은 숫자를 print한다.
맨 왼쪽 위 칸이 흰색인 경우와 검은색인 경우 두 가지가 있는데,
이것은 직접 구하는 것보다 흰색인 경우 칠해야 하는 수를 구한 다음에 M\*N - 흰색칠할수 를 하면 검은색일 경우 칠해야 하는 수를 구할 수있다.

```python
import sys

N, M = [int(num) for num in sys.stdin.readline().split()]
board = []
result = 64
for line in sys.stdin.readlines():
    board.extend(line.rsplit())

for start_row in range(0, N - 7):
    end_row = start_row + 8
    for start_col in range(0, M - 7):
        end_col = start_col + 8
        white = 0
        new_board = [row[start_col:end_col] for row in board[start_row:end_row]]
        for rindex, row in enumerate(new_board):
            for cindex, color in enumerate(row):
                if ((rindex + cindex) % 2 == 0 and color == "W") or (
                    (rindex + cindex) % 2 == 1 and color == "B"
                ):
                    white += 1
        black = 64 - white
        minimum = min(white, black)
        result = min(minimum, result)
print(result)

```

혹은 매번 반복하지 않고 입력받을때 start_col부터 end_col까지의 칠해야하는 수를 구하고, 이것을 리스트화한다
만약 10 x 10 의 체스판을 리스트화 한다면
BBBBBBBBBB -> [4, 4, 4] (0 ~ 8, 1 ~ 9, 2 ~ 10)
BBWBWBWBWB -> [7, 8, 8] (0 ~ 8, 1 ~ 9, 2 ~ 10)
BWBWBWBWBB -> [8, 8, 7] (0 ~ 8, 1 ~ 9, 2 ~ 10)
BBWBWBWBWB -> [7, 8, 8] (0 ~ 8, 1 ~ 9, 2 ~ 10)
BWBWBWBWBB -> ...
BBWBWBWBWB -> ...
BWBWBWBWBB
BBWBWBWBWB
BWBWBWBWBB
BBBBBBBBBB
이런 식이다. 그리고 이 리스트의 같은 인덱스끼리 수를 묶어서 더한다
그러면 white를 칠하는데 필요한 값들이 나온다. 이것은
4 x 4 배열로 표현된다. 이 배열 안에 들어있는 숫자의 가장 큰 수와 가장 작은 수를 구한 후, 64에서 가장 큰 수를 뺀 수와 가장 작은 수를 비교하면 답이 나온다.
이런 알고리즘으로 한다면 약간 더 빠른 알고리즘이 나올것이다.
속도차이가 거의 안났다.

```python
import sys

N, M = [int(num) for num in sys.stdin.readline().split()]
sum_rows = []
result = 64
for line in sys.stdin.readlines():
    sum_row = []
    for row_start in range(M - 7):
        row_end = row_start + 8
        sum_row.append(
            sum(
                1
                for cindex, color in enumerate(line[row_start:row_end])
                if ((len(sum_rows) + cindex) % 2 == 0 and color == "W")
                or ((len(sum_rows) + cindex) % 2 == 1 and color == "B")
            )
        )
    sum_rows.append(sum_row)

sum_matrix = []
for cindex in range(M - 7):
    for row_start in range(N - 7):
        row_end = row_start + 8
        sum_cols = [sum(row) for row in zip(*sum_rows[row_start:row_end])]
        sum_matrix.extend(sum_cols)
print(min(64 - max(sum_matrix), min(sum_matrix)))

```

[1]: https://www.acmicpc.net/problem/1018

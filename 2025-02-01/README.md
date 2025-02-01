# 코딩 테스트에 도움이 되는 개념들

## **1. 삼각수의 성질**

- **정의**: 1부터 n까지의 자연수를 모두 더한 값입니다.
- **공식**: \( T_n = \frac{n(n + 1)}{2} \)
- **활용**:
  - 반복문 없이 합을 빠르게 계산할 때 사용합니다.
  - 대각선 그룹을 계산하거나 패턴 분석에 유용합니다.

### 예시:

```python
def triangular_number(n):
    return n * (n + 1) // 2

print(triangular_number(10))  # 출력: 55
```

---

## **2. `divmod()` 함수**

- **기능**: 몫과 나머지를 동시에 반환합니다.
- **활용**:
  - 나눗셈과 나머지 연산이 동시에 필요한 경우에 유용합니다.
  - 진법 변환, 시간 계산 등 다양한 문제에서 사용됩니다.

### 예시:

```python
quotient, remainder = divmod(17, 5)
print(quotient, remainder)  # 출력: 3 2
```

---

## **3. 진법 변환**

- **10진수를 n진수로 변환**:
  - `divmod()`를 사용하여 몫과 나머지를 반복적으로 계산합니다.
  - 나머지를 역순으로 나열하면 n진수가 됩니다.

### 예시:

```python
def decimal_to_base_n(decimal, base):
    digits = []
    while decimal > 0:
        decimal, remainder = divmod(decimal, base)
        digits.append(remainder)
    return ''.join(str(d) for d in digits[::-1])

print(decimal_to_base_n(25, 2))  # 출력: 11001
```

---

## **4. 10진수를 n진수로 변환하는 법**

- **단계**:
  1. 10진수를 n으로 나누어 나머지를 기록합니다.
  2. 몫이 0이 될 때까지 반복합니다.
  3. 나머지를 역순으로 나열합니다.

### 예시:

```python
def decimal_to_base_n(decimal, base):
    if decimal == 0:
        return "0"
    digits = []
    while decimal > 0:
        decimal, remainder = divmod(decimal, base)
        if remainder >= 10:
            digits.append(chr(ord('A') + remainder - 10))  # 10 이상은 알파벳으로
        else:
            digits.append(str(remainder))
    return ''.join(reversed(digits))

print(decimal_to_base_n(255, 16))  # 출력: FF
```

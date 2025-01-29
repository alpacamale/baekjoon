#!/usr/bin/env python
import os
import sys
from datetime import datetime
import requests
import time
from bs4 import BeautifulSoup
from config import user_agent

# 잘못된 입력이 있을 시 종료
if len(sys.argv) != 2:
    print("Usage: ./mk2folder.py [number]")
    sys.exit(1)

number = sys.argv[1]
url = f"https://www.acmicpc.net/problem/{number}"
headers = {"User-Agent": user_agent}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
description = "\n".join(p.text.strip() for p in soup.select("#problem_description > *"))
input = soup.select_one("#problem_input > p").text.strip()
output = soup.select_one("#problem_output > p").text.strip()
sample_input = soup.select_one("#sample-input-1").text.rstrip()
sample_output = soup.select_one("#sample-output-1").text.rstrip()

markdown = f"""# {number}

[코딩테스트 연습 - {number}][1] 로 이동

## 문제

{description}

## 입력

{input}

## 출력

{output}

## 예제 입력

```
{sample_input}
```

## 예제 출력

```
{sample_output}
```

## 풀이

```python

```

[1]: {url}"""

# 디렉토리와 python 파일, README 생성
date = datetime.today().strftime("%Y-%m-%d")
os.makedirs(date, exist_ok=True)
os.makedirs(f"{date}/{number}", exist_ok=True)
with open(f"{date}/README.md", "a", encoding="utf-8") as file:
    pass
with open(f"{date}/{number}/{number}.py", "w") as file:
    pass
with open(f"{date}/{number}/README.md", "w", encoding="utf-8") as file:
    file.write(markdown)

# 완료 메시지 출력
print(f"Folder and structure created at {date}/{number}.")
print(f"The Python command is: python {date}/{number}/{number}.py")

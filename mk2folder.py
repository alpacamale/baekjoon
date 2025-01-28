#!/usr/bin/env python
import os
import sys
from datetime import datetime
import requests
import time
from bs4 import BeautifulSoup
from config import user_agent

if len(sys.argv) != 2:
    print("Usage: ./mk2folder.py [number]")
    sys.exit(1)

number = sys.argv[1]
url = f"https://www.acmicpc.net/problem/{number}"
headers = {"User-Agent": user_agent}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
description = soup.select_one("#problem_description > p").text.strip()
input = soup.select_one("#problem_input > p").text.strip()
output = soup.select_one("#problem_output > p").text.strip()
sample_input = soup.select_one("#sample-input-1").text.strip()
sample_output = soup.select_one("#sample-output-1").text.strip()

markdown = f"""
# {number}

[코딩테스트 연습 - $1][1] 로 이동

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
```

```

[1]: {url}
"""

date = datetime.today().strftime("%Y-%m-%d")
os.makedirs(date, exist_ok=True)
os.makedirs(f"{date}/{number}", exist_ok=True)

with open(f"{date}/{number}/{number}.py", "w") as file:
    pass
with open(f"{date}/{number}/README.md", "w", encoding="utf-8") as file:
    file.write(markdown)


print(f"Folder and structure created at {date}/{number}.")

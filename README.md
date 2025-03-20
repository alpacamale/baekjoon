# 백준 온라인 저지 문제 풀이

이 레포지토리는 [백준 온라인 저지](https://www.acmicpc.net/)에서 제공하는 다양한 문제들의 풀이를 담고 있습니다. 여러 프로그래밍 언어로 구현된 풀이들이 문제 번호별로 정리되어 있습니다.

## 폴더 구조

```
├── YYYY-MM-DD/
│   ├── README.md
│   ├── 문제이름1/
│   │   ├── 문제이름1.py
│   │   ├── README.md
│   ├── 문제이름2/
│   │   ├── 문제이름2.py
│   │   ├── README.md
│   └── ...
```

## 💲 파이썬 스크립트

폴더 구조를 자동으로 만들기 위해서 스크립트를 만들었습니다.

```
mk2folder 문제번호
```

명령어를 실행하여

```
.
├── YYYY-MM-DD/
| ├── 문제번호/
| │ ├── 문제번호.py
| │ └── README.md # 풀이 설명
```

의 폴더 구조를 생성하고, 백준 웹페이지에서 해당 문제에 대한 설명, 인풋 아웃풋의 조건을 자동으로 스크래핑하여 README.md 를 작성합니다.

## 문제 풀이

각 문제별로 풀이 코드를 제공하며, 문제에대한 설명과 함께 시간 복잡도 및 해결 방법도 함께 정리합니다.

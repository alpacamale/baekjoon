# 백준 온라인 저지 문제 풀이

이 레포지토리는 [백준 온라인 저지](https://www.acmicpc.net/)에서 제공하는 다양한 문제들의 풀이를 담고 있습니다. 여러 프로그래밍 언어로 구현된 풀이들이 문제 번호별로 정리되어 있습니다.

## 목차

- [폴더 구조](#폴더-구조)
- [쉘 스크립트](#-쉘-스크립트)
- [문제 풀이](#문제-풀이)
- [사용 언어](#-사용-언어)
- [날짜 포멧](#날짜-포멧)

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

## 💲 쉘 스크립트

폴더 구조를 자동으로 만들기 위해서 스크립트를 만들었습니다.

```
./mk2folder.sh 문제번호
```

명령어를 실행하여

```
.
├── YYYY-MM-DD/
| ├── 문제번호/
| │ ├── 문제번호.py
| │ └── README.md # 풀이 설명
```

의 폴더 구조를 생성할 수 있습니다.

## 문제 풀이

각 문제별로 풀이 코드를 제공하며, 문제에대한 설명과 함께 시간 복잡도 및 해결 방법도 함께 정리합니다.

## ⭐ 사용 언어

- 파이썬

## 날짜 포멧

커밋 메시지에 사용되는 날짜 포멧은 YYYY-MM-DD 입니다.

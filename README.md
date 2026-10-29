# AWS EC2 기반 Nginx 로그 분석 자동화

## 1. 프로젝트 소개

AWS EC2의 Ubuntu Linux 환경에서 Nginx 웹서버를 구축하고, Python을 활용해 HTTP 접근 로그를 분석하는 프로젝트입니다.

Linux의 crontab을 활용하여 로그 분석 작업을 주기적으로 실행하도록 자동화했습니다.

## 2. 프로젝트 목표

- AWS EC2 기반 Linux 웹서버 구축 및 운영
- Nginx Access Log 수집 및 분석
- Python을 활용한 HTTP 요청 및 오류 통계 분석
- 반복적인 404 오류 요청 탐지
- crontab을 활용한 정기적인 로그 분석 자동화

## 3. 사용 기술

| 구분 | 사용 기술 |
|---|---|
| Cloud | AWS EC2 |
| OS | Ubuntu Linux |
| Web Server | Nginx |
| Programming | Python 3 |
| Automation | cron / crontab |
| Version Control | Git / GitHub |

## 4. 주요 구현 기능

**① HTTP 상태 코드 분석**

- HTTP 상태 코드별 요청 횟수 집계
- 4xx 및 5xx 오류율 계산

**② 클라이언트 요청 분석**

- 요청 횟수가 많은 상위 5개 IP 확인
- 요청 빈도가 높은 상위 5개 URL 확인

**③ 반복적인 404 오류 탐지**

- IP별 404 오류 발생 횟수 집계
- 동일 IP에서 404 오류가 5회 이상 발생하면 확인 대상 표시

**④ 로그 분석 자동화**

- Python 스크립트를 사용한 Nginx 로그 분석
- crontab을 통한 주기적인 분석 작업 실행

## 5. 시스템 구성

HTTP 요청 → AWS EC2 / Nginx → access.log → Python 로그 분석 → 분석 결과 출력

cron을 사용하여 Python 분석 작업을 예약 실행합니다.

## 6. 실행 방법

Nginx 접근 로그를 Python 프로그램의 표준 입력으로 전달하여 분석합니다.

`sudo cat /var/log/nginx/access.log | python3 analyzer.py`

실행 시 HTTP 상태 코드 통계, 클라이언트 IP별 요청 횟수, URL별 요청 횟수, 오류율 및 반복 404 탐지 결과를 확인할 수 있습니다.

## 7. 실행 결과

<img width="1891" height="897" alt="파이썬 로그분석" src="https://github.com/user-attachments/assets/3593ed29-0a0e-46a2-8396-f6cd3d673c0c" />


## 8. 향후 개선 계획

- CSV 형식의 분석 결과 저장 기능
- 특정 시간 구간별 요청 빈도 분석
- 이상 접근 발생 시 알림 기능 추가


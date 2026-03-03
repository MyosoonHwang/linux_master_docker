# 🐧 Genius Linux: AI-Powered Linux Master Prep
Gemini 2.5 AI 기반 오답 해설 기능을 탑재한 리눅스 마스터 2급 자격증 대비 웹 애플리케이션

## 왜 만들었는가?
### 1. 자격증 취득의 효율성 극대화
### 리눅스 마스터 2급 자격증을 준비하며, 단순히 답안지만 보고 정답을 외우는 기존 방식의 한계를 느꼈습니다.

### "왜 이 답이 틀렸는지"에 대해 즉각적이고 논리적인 피드백을 받기 위해, 최신 AI 모델인 Gemini 2.5를 학습 보조 도구로 도입했습니다.

### 2. 클라우드 엔지니어(Cloud SE)로서의 역량 증명
### 단순한 코딩 능력을 넘어, 실제 인프라 환경에서 앱이 어떻게 동작하고 배포되는지 증명하고자 했습니다.

### Docker를 통한 컨테이너 최적화, MySQL 데이터베이스 설계, requirements.txt를 통한 의존성 관리 등 실무적인 백엔드 아키텍처를 직접 구축하는 경험을 쌓고자 했습니다.

### 3. AI 기술의 실무적 적용 연습
### 텍스트 생성 인공지능(LLM)을 실제 서비스에 어떻게 접목할 수 있을지 고민했습니다.

### 문제 생성의 불안정성을 줄이기 위해 문제는 고정 DB에서 불러오고, 해설에만 AI를 집중시키는 '하이브리드 방식'을 선택하여 시스템의 안정성을 확보하는 엔지니어링적 판단을 연습했습니다.

## 🚀 프로젝트 개요
리눅스 마스터 2급 자격증 취득을 준비하는 수험생들을 위해, 단순한 문제 풀이를 넘어 AI가 틀린 원인을 분석하고 맞춤형 해설을 제공하는 효율적인 학습 도구입니다. 경량화된 Docker 환경을 지원하여 클라우드 환경 어디서든 즉시 배포 및 실행이 가능하도록 설계되었습니다.

## ✨ 주요 기능 (Key Features)
고정 기출문제 세트: 엄선된 리눅스 마스터 2급 핵심 기출문제 20문항을 제공합니다.

AI 맞춤형 해설: Google Gemini 2.5 Flash-Lite 모델을 연동하여, 사용자가 선택한 오답의 원인을 분석하고 정답의 핵심 개념을 요약해 줍니다.

지능형 오답 저장소: 틀린 문제는 자동으로 데이터베이스에 기록되며, 언제든지 다시 확인하고 AI 해설을 요청할 수 있습니다.

학습 가이드 제공: 시험 일정에 따른 D-Day 계산 및 AI의 합격 전략 조언 기능을 제공합니다.

유튜브 연동 학습: 오답 개념과 관련된 유튜브 강의 검색 링크를 자동으로 생성하여 추가 학습을 돕습니다.

## 🛠 기술 스택 (Tech Stack)
### Backend
Language: Python 3.14.3

Framework: Flask

ORM: SQLAlchemy

Database: SQLite (Development) / MySQL (Production Ready)

AI SDK: google-genai (Latest Version)

#### Infrastructure
Container: Docker (python:3.14.3-slim)

VCS: GitHub

⚙️ 실행 방법 (Getting Started)
1. 로컬 환경 실행
```Bash
# 의존성 설치
pip install -r requirements.txt

# DB 초기화 및 문제 삽입 (중요)
python seed_db.py

# 앱 실행
python run.py
```
2. Docker 환경 실행
```Bash
# 이미지 빌드
docker build -t linux-master-app .

# 컨테이너 실행
docker run -d -p 5000:5000 --name linux-app linux-master-app
```

📁 프로젝트 구조 (Project Structure)
## 📁 프로젝트 구조 (Project Structure)
```plaintext
.
├── app/
│   ├── models.py          # SQLAlchemy DB 모델 정의
│   ├── routes/
│   │   └── main.py        # 핵심 비즈니스 로직 및 라우팅
│   ├── services/
│   │   └── gemini_service.py # Gemini AI API 연동부
│   └── templates/         # Jinja2 템플릿 파일
├── Dockerfile             # 경량화 빌드 설정
├── requirements.txt       # 패키지 의존성 목록
├── seed_db.py             # 초기 데이터 삽입 스크립트
└── run.py                 # 애플리케이션 엔트리 포인트
```

👤 Author
MyosoonHwang - GitHub
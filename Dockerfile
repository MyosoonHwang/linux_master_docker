# --- Stage 1: Builder (패키지 설치 단계) ---
FROM python:3.14.3-slim AS builder

WORKDIR /app
COPY requirements.txt .

# 빌드 도구를 사용하여 패키지를 특정 폴더(/install)에 설치
RUN pip install --upgrade pip && \
    pip install --no-cache-dir --prefix=/install -r requirements.txt

# --- Stage 2: Runner (최종 경량화 이미지) ---
FROM python:3.14.3-slim

WORKDIR /app

# 환경 변수 설정
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 빌더 스테이지에서 설치된 패키지만 쏙 빼오기 (이것이 핵심!)
COPY --from=builder /install /usr/local
# 소스 코드 복사
COPY . .

EXPOSE 5000
CMD ["python", "run.py"]
import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

class Config:
    # 환경 변수에서 정보를 가져와 DB URI 생성
    user = os.getenv('DB_USER')
    pw = os.getenv('DB_PASSWORD')
    host = os.getenv('DB_HOST')
    db_name = os.getenv('DB_NAME')
    
    # mysql+pymysql://사용자:비밀번호@호스트/DB이름
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{user}:{pw}@{host}/{db_name}?charset=utf8mb4'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
    SECRET_KEY = os.getenv('SECRET_KEY')
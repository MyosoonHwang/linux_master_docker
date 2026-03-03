from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone

db = SQLAlchemy()

# 1. 고정된 기출문제를 저장하는 테이블
class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    choices = db.Column(db.JSON, nullable=False)  # ['1번보기', '2번보기', '3번보기', '4번보기']
    answer = db.Column(db.Integer, nullable=False)
    concept = db.Column(db.String(100))

# 2. 사용자가 틀린 문제를 저장하는 테이블
class WrongAnswer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    choices = db.Column(db.JSON, nullable=False)
    correct_answer = db.Column(db.Integer, nullable=False)
    user_answer = db.Column(db.Integer, nullable=False)
    concept = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
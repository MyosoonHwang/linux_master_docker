from flask import Flask
from config import Config
from .models import db  # models.py에서 생성한 db를 가져옵니다.

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # DB 초기화
    db.init_app(app)

    # Blueprint 등록 (순환 참조 방지를 위해 함수 내부에서 import)
    from .routes.main import main_bp
    app.register_blueprint(main_bp)

    return app
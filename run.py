from app import create_app
from app.models import db

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        # 테이블 자동 생성
        db.create_all()
    app.run(debug=True)
from app import create_app
from app.models import db
import os

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        # 테이블 자동 생성
        # 주의: DB_HOST가 host.docker.internal로 되어 있어야 에러 없이 통과합니다.
        db.create_all()
    
    # 수정된 부분: host='0.0.0.0'을 추가해야 도커 외부에서 접속 가능합니다.
    app.run(host='0.0.0.0', port=5000, debug=True)
from werkzeug.security import generate_password_hash
from app import app
from models import db, User

USERNAME = "user1"
PASSWORD = "pw1234!"


with app.app_context():
    if User.query.filter_by(username=USERNAME).first():
        print(f"[SKIP] 이미존재: {USERNAME}")
    else:
        u = User(username=USERNAME, password=generate_password_hash(PASSWORD))
        db.session.add(u)
        db.session.commit()
        print(f"[OK] 사용자 생성: {USERNAME}")
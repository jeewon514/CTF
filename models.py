from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#사용자 모델
class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    score = db.Column(db.Integer, default=0)
    
# 문제 모델
class Challenge(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text)
    flag = db.Column(db.String(200))
    points = db.Column(db.Integer)

# 제출 기록 모델
class Submission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    challenge_id = db.Column(db.Integer, db.ForeignKey('challenge.id'))
    submitted_flag = db.Column(db.String(200))
    correct = db.Column(db.Boolean)
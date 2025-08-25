from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User, Challenge, Submission

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ctf.db'
app.config['SECRET_KEY'] = 'secret_key_here'

db.init_app(app)            # DB 초기화 연결


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET','POST'])
def login():
    # POST
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            flash('로그인 성공')
            return redirect(url_for('challenges'))
        else:
            flash('아이디 또는 비밀번호가 올바르지 않습니다.')
            return render_template('user.html')
    # GET
    return render_template('login.html')


@app.route('/challenges')
def challenges():
    challenges = Challenge.query.all()
    return render_template('challenge.html', challenges=challenges)





@app.route('/scoreboard')
def scoreboard():
    users = User.query.order_by(User.score.desc()).all()
    return render_template('scoreboard.html', users=users)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
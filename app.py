from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User, Challenge, Submission

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ctf.db'
app.config['SECRET_KEY'] = 'secret_key_here'
app.secret_key = "dev"          # flash 사용 시 필요

db.init_app(app)                # DB 초기화 연결

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


# 템플릿의 url_for('submit', challenge_id=...) 와 정확히 일치하는 라우트
@app.route('/submit/<int:challenge_id>', methods=['POST'])
def submit(challenge_id):
    if 'user_id' not in session:
        flash('로그인이 필요합니다.')
        return redirect(url_for('login'))

    raw = request.form.get('flag', '')
    submitted = normalize(raw)
    chal = Challenge.query.get_or_404(challenge_id)
    answer = normalize(chal.flag)

    user = User.query.get(session['user_id'])
    if user is None:
        flash('세션 사용자 정보를 찾을 수 없습니다.')
        return redirect(url_for('login'))

    # 이미 정답 처리했는지 확인
    already = Submission.query.filter_by(
        user_id=user.id, challenge_id=chal.id, correct=True
    ).first()

    is_correct = (submitted == answer)  # 완전 일치(정규화 후). 대소문자 무시하려면 .lower()로 비교.

    # 제출 기록 저장(정답/오답 모두)
    sub = Submission(
        user_id=user.id,
        challenge_id=chal.id,
        submitted_flag=raw,   # 원문 그대로 보관
        correct=is_correct
    )
    db.session.add(sub)

    if is_correct:
        if already:
            flash('이미 푼 문제입니다. 점수는 한 번만 적립됩니다.')
            db.session.commit()
            return redirect(url_for('challenges'))
        # 최초 정답 → 점수 적립
        user.score = (user.score or 0) + (chal.points or 0)
        db.session.commit()
        flash(f'정답입니다! +{chal.points}점 적립')
        return redirect(url_for('scoreboard'))
    else:
        db.session.commit()
        # 디버깅용: 제출값과 정답을 살짝 보여 줌(개발 중에만)
        flash(f'오답입니다. 제출="{submitted}" / 정답="{answer}"')
        return redirect(url_for('challenges'))


@app.route('/scoreboard')
def scoreboard():
    users = User.query.order_by(User.score.desc()).all()
    return render_template('scoreboard.html', users=users)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
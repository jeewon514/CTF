from app import app
from models import db, Challenge

with app.app_context():
    if Challenge.query.count() == 0:
        problems = [
            Challenge(
                title="Base64 Warmup",
                description=(
                    "[Crypto] Base64 Warmup\n"
                    "아래 문자열을 Base64로 디코딩하면 플래그가 나옵니다.\n\n"
                    "ZmxhZ3tNaW5pX0Jhc2U2NF9XYXJtdXB9\n\n"
                    "플래그 형식: flag{...}"
                ),
                flag="flag{Mini_Base64_Warmup}",
                points=100
            ),
            Challenge(
                title="[Crypto] ROT13",
                description=(
                    "다음 문장을 ROT13으로 복호화하세요.\n\n"
                    "synt{ZvavVqragFhofgne}\n\n"
                    "힌트: 알파벳 13자리씩 치환."
                ),
                flag="flag{MingHiddenSubtar}",
                points=150
            ),
            Challenge(
                title="[Forensic] Hex to ASCII",
                description=(
                    "다음 16진수를 ASCII로 변환하면 플래그가 나옵니다.\n\n"
                    "66 6C 61 67 7B 48 65 78 5F 52 65 61 64 7D"
                ),
                flag="flag{Hex_Read}",
                points=150
            ),
        ]

        db.session.add_all(problems)
        db.session.commit()
        print("[OK] 예시 문제 3개 생성 완료")
    else:
        print("[SKIP] 이미 문제가 존재합니다.")
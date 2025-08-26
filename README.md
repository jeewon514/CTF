## 🔉CTF 연습 PlatForm
>사용자가 문제를 풀고 플래그를 제출하면 DB에 점수가 기록되고, Scoreboard에 반영되는 CTF 플랫폼을 구현한 프로젝트
- Hopy 25-1 여름방학 프로젝트
- 컴퓨터공학과 & 사이버보안과

</br>

## 🛠 기술 스택
**Environment**

<img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> <img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white"> <img src="https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=white">

**Development**

<img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white"> <img src="https://img.shields.io/badge/css-1572B6?style=for-the-badge&logo=css3&logoColor=white"> <img src="https://img.shields.io/badge/flask-000000?style=for-the-badge&logo=flask&logoColor=white">

</br>

## ⚙️설치 & 실행 (Installation & Usage)
- flask 프로젝트 생성
> python -m venv venv
> source venv\Scripts\activate
> pip install flask flask-login flask-sqlalchemy (패키지 설치)

</br>

## 📂 프로젝트 구조 (Project Structure)
```bash
📦 CTF
 ┣ 📂 static
 ┃ ┣ 📜 styles.css
 ┣ 📂 templates
 ┃ ┣ 📜 base.html
 ┃ ┗ 📜 challenge.html
 ┃ ┗ 📜 index.html
 ┃ ┗ 📜 login.html
 ┃ ┗ 📜 scoreboard.html
 ┣ 📂venv
 ┃ ┗ 📜 Include
 ┃ ┗ 📜 Lib
 ┃ ┗ 📜 Scripts
 ┃ ┗ 📜 scoreboard.html
 ┃ 📂 .gitignore
 ┃ 📜 app.py
 ┃ 📜 create_challenge.py
 ┃ 📜 create_users.py
 ┃ 📜 models.py
 ┗ 📜 README.md

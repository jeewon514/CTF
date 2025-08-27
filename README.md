## 🔉CTF 연습 PlatForm 
>사용자가 문제를 풀고 플래그를 제출하면 DB에 점수가 기록되고, Scoreboard에 반영되는 CTF 플랫폼을 구현한 프로젝트
- Hopy 25-1 여름방학 프로젝트
- 컴퓨터공학과 & 사이버보안과

</br>

## 🚀 About (소개)
사용자가 문제를 풀고 플래그를 제출하면 점수가 기록되는 시스템입니다. 

- 🎯 목표: 웹 기반 CTF(Capture The Flag) 플랫폼 구현
- 🧩 특징: CTF 문제 DB에 등록/ 서버에서 정답 여부 확인/정답 시 DB에 점수 집계 반영
  
</br>

## ✨ Features (기능)
| 기능 | 설명 | 상태 |
|------|------|------|
| 🔐 로그인 | 사용자 인증 및 세션 관리 | ✅ 완료 |
| 📝 문제 등록 | 관리자 문제 업로드 기능 | ✅ 완료 (업로드 기능 제외, DB에서 문제를 바로 올리기) |
| 🎮 문제 풀이 | 사용자 플래그 제출 및 검증 | ✅ 완료 |
| 🏆 스코어보드 | 순위 확인 기능 | ✅ 완료 |
| 📦 파일 암호화 | 업로드 시 AES 암호화 적용 | 🔜 예정 |

</br>

## 🛠 Tech Stack (기술 스택)
**Frontend**
</br>
<img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white"> <img src="https://img.shields.io/badge/css-1572B6?style=for-the-badge&logo=css3&logoColor=white">


**Backend**
</br>
 <img src="https://img.shields.io/badge/flask-000000?style=for-the-badge&logo=flask&logoColor=white"> <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white">


**Database**
</br>
 <img src="https://img.shields.io/badge/sqlalchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white"> 

</br>

## ⚙️설치 & 실행 (Installation & Usage)
- flask 프로젝트 설치
> python -m venv venv </br>
> source venv\Scripts\activate </br>
> pip install flask flask-login flask-sqlalchemy </br>

</br>

- 프로젝트 실행
> python app.py </br>
> 브라우저에서 http://localhost:5000 접속

</br>

## 🧑‍💻 Contributor
- [구지원](https://github.com/jeewon514)

</br>

## 📄 Documents (문서)
- [프로젝트 보고서 PDF](https://github.com/jeewon514/CTF/blob/main/docs/CTF_Platform.pdf)

</br>

## 📂 Project Structure
```bash
📦 CTF
 ┣ 📂 docs
 ┃ ┣ 📜 CTF_platform.pdf
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

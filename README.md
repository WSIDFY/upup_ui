```
project-root/
├── app_ui/
│   ├── public/            # 정적 파일
│   ├── src/               # 소스 코드
│   │   ├── assets/        # 이미지, 폰트 등
│   │   ├── components/    # 재사용 가능한 컴포넌트
│   │   ├── pages/         # 페이지 컴포넌트
│   │   ├── services/      # API 호출 관련 서비스
│   │   ├── context/       # 상태 관리
│   │   ├── App.jsx        # .js 대신 .jsx 확장자가 기본
│   │   ├── main.jsx       # CRA의 index.js에 해당
│   │   └── index.css      # 기본 스타일
│   ├── index.html         # 진입점 HTML
│   ├── vite.config.js     # Vite 설정 파일
│   ├── package.json
│   └── README.md
├── app_server/                          # FastAPI 백엔드
│   ├── app/
│   │   ├── api/
│   │   │   ├── v1/
│   │   │   │   ├── endpoints/
│   │   │   │   │   ├── file.py           # 파일 업로드/처리 API
│   │   │   │   │   ├── quiz.py           # 퀴즈 생성/풀이 API
│   │   │   │   │   └── __init__.py
│   │   │   │   └── __init__.py
│   │   ├── core/
│   │   │   ├── config.py                 # 환경 변수 로딩
│   │   │   └── database.py               # SQLAlchemy DB 연결
│   │   ├── models/
│   │   │   ├── file.py
│   │   │   ├── quiz.py
│   │   │   └── __init__.py
│   │   ├── schemas/
│   │   │   ├── file.py
│   │   │   ├── quiz.py
│   │   │   └── __init__.py
│   │   ├── services/
│   │   │   ├── file_service.py           # 텍스트 추출 로직
│   │   │   ├── quiz_service.py           # GPT 퀴즈 생성 로직
│   │   │   └── gpt_client.py             # OpenAI API 호출
│   │   ├── utils/
│   │   │   └── file_parser.py            # .hwp/.pdf 등 텍스트 파서
│   │   └── main.py                       # FastAPI 앱 진입점
│   ├── .env
│   ├── requirements.txt
│   └── README.md

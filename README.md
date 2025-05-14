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
├── app_server/                 # Express 백엔드
│   ├── config/             # 설정 파일
│   │   └── db.js           # MongoDB 연결 설정
│   ├── controllers/        # 라우트 컨트롤러
│   │   ├── authController.js
│   │   ├── userController.js
│   │   ├── postController.js
│   │   └── commentController.js
│   ├── middleware/         # 미들웨어
│   │   ├── auth.js         # 인증 미들웨어
│   │   └── errorHandler.js
│   ├── models/             # MongoDB 모델
│   │   ├── User.js
│   │   ├── Post.js
│   │   └── Comment.js
│   ├── routes/             # API 라우트
│   │   ├── authRoutes.js
│   │   ├── userRoutes.js
│   │   ├── postRoutes.js
│   │   └── commentRoutes.js
│   ├── utils/              # 유틸리티 함수
│   │   └── validators.js
│   ├── app.js              # Express 앱 설정
│   ├── server.js           # 서버 시작점
│   ├── package.json
│   └── .env                # 환경 변수 (git에 포함하지 않음)
├── .gitignore
└── README.md
```

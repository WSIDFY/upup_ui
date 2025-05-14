'use client';

import QuizUI from '../components/QuizUI';
import styles from '../styles/quiz.module.css'; // 스타일 추가

export default function QuizPage() {
  return (
    <div className={styles.quizPageWrapper}>
      <QuizUI />        {/*QuizUI.jsx 받아와서 렌더링*/}
    </div>
  );
}




// 퀴즈 생성 페이지의 테스트 코드입니다!
//'use client';

//import QuizUI from '../components/QuizUI';
//import styles from '../styles/quiz.module.css';

// 샘플 데이터를 정의합니다/
//const sampleData = {
//  filename: "정보검색론 중간고사",
//  question: "문제의 길이가 길어질 때 개행이 실행되는지 파악하기 위해 문제의 내용을 늘리고 있다고 할 때, 다음 중 정보처리 기사단의 팀원으로 올바르지 않은 사람은?",
//  options: [
//    { text: "김민성", is_correct: false },
//    { text: "장민재", is_correct: false },
//    { text: "박민재", is_correct: true },  // 정답 문항 3번
//    { text: "김민재", is_correct: false }
//  ],
//  explanations: [ // 채점시 해설 내용
//    "김민성은 정보처리기사단의 든든한 기사이기 때문에 오답입니다.",
//    "장민재는 정보처리 기사단의 날렵한 궁수이기 때문에 오답입니다.",
//    "박민재는 모르는 사람이기 때문에 오답입니다.",
//    "김민재는 정보처리 기사단의 기사 견습생이기 때문에 오답입니다."
//  ]
//};

//export default function QuizPage() {
//  return (
//    <div className={styles.quizPageWrapper}>
//      <QuizUI quizData={sampleData} />  {/*샘플 데이터를 적용하여 퀴즈 생성 페이지를 렌더링 합니다.*/}
//    </div>
//  );
//}
import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def grade_answer(question: str, choices: list, user_answer: str) -> dict:
    prompt = f"""
아래는 객관식 문제입니다. 사용자의 선택이 정답인지 판단하고, 해설도 제공해주세요.

문제:
{question}

보기:
{chr(65)}. {choices[0]}
{chr(66)}. {choices[1]}
{chr(67)}. {choices[2]}
{chr(68)}. {choices[3]}

사용자 선택: {user_answer}

결과는 JSON 형식으로 알려줘. 형식:
{{
  "is_correct": true or false,
  "correct_answer": "C",
  "explanation": "왜 그런지 설명"
}}
"""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
        max_tokens=500
    )

    import json
    return json.loads(response.choices[0].message["content"])

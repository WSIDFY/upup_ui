import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_quiz_from_text(text: str) -> str:
    prompt = f"""
다음 텍스트를 기반으로 대학생 수준의 객관식 문제 3개를 만들어줘.
각 문제는 4개의 보기와 정답 번호, 해설을 포함해줘.
{text}
"""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=1000,
    )
    return response.choices[0].message["content"]




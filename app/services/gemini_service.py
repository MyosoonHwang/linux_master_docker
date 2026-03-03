import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

def get_wrong_answer_explanation(question, correct_ans, user_ans):
    """사용자가 틀린 문제에 대해 명쾌한 해설을 제공합니다."""
    model = genai.GenerativeModel('gemini-2.5-flash')
    
    prompt = f"""
    리눅스 마스터 2급 문제입니다.
    - 문제: {question}
    - 정답: {correct_ans}
    - 사용자가 고른 오답: {user_ans}
    
    사용자가 왜 이 오답을 골랐을지 짚어주고, 정답이 왜 정답인지 핵심 개념을 3줄 이내로 명확하게 해설해줘.
    """
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return "해설을 불러오는 중 오류가 발생했습니다."
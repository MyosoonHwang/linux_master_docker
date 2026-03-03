import os
import google.generativeai as genai
from dotenv import load_dotenv

# .env 로드 및 설정
load_dotenv()
api_key = os.getenv('GEMINI_API_KEY')

if not api_key:
    print("Error: .env 파일에 GEMINI_API_KEY가 없습니다.")
else:
    genai.configure(api_key=api_key)

    print(f"{'Model Name':<30} | {'Supported Methods'}")
    print("-" * 60)

    try:
        # 사용 가능한 모델 리스트 출력
        for m in genai.list_models():
            # 텍스트 생성이 가능한 모델만 필터링
            if 'generateContent' in m.supported_generation_methods:
                print(f"{m.name:<30} | {m.supported_generation_methods}")
    except Exception as e:
        print(f"모델 목록을 가져오는 중 오류 발생: {e}")
# sentiment_analysis.py
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# OpenAI API 키 설정 (환경 변수로 설정 권장)

def analyze_sentiment(text):
    prompt = '''아래 뉴스에서 S&P500에 상장된 기업명을 모두 추출하고, 기업에 해당하는 감성을 분석하시오.
각 감성에 스코어링을 하시오. 각 스코어의 합은 1이 되어야 합니다. 소수점 첫번째까지만 생성하세요.
출력포맷은 리스트이며, 세부 내용은 다음과 같습니다.
반드시 출력포맷만을 생성하시오. 그 이외의 단어나 설명은 생성하지마시오.
[{"organization": <기업명>, "positive": 0~1, "negative": 0~1, "neutral": 0~1}, ...]

뉴스: '''

    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt + text}
    ]
    try:
        response = client.chat.completions.create(model="gpt-4o-mini",
        messages=messages)
        answer = response.choices[0].message.content
        sentiments = eval(answer)
        return sentiments
    except Exception as e:
        print(f"Error in sentiment analysis: {e}")
        return []

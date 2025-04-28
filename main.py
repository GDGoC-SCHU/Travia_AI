from gemini_api_client import generate_travel_recommendation
from pprint import pprint

# 테스트용 프롬프트 (예시)
test_prompt = """
다음은 한 여행자의 성향 정보입니다:

- 동행: 커플
- 여행 스타일: 감성, 먹방
- 여행 기간: 4박 5일
- 운전 여부: 불가능
- 예산: 1500000원
- 선호 기후: 따뜻한 곳
- 대륙 선호: 동남아
- 하루 활동 밀도: 적당히

이 사용자의 성향에 맞는 세계 여행 도시 2~3곳을 추천해주세요.

반드시 아래와 같은 **JSON 형식**으로 응답해 주세요.

```json
{
  "data": [
    {
      "city": "도시 이름",
      "country": "국가",
      "reason": "성향과의 매칭 이유를 간결하게 설명",
      "schedule": {
        "day_1": [
          { "time": "10:00-13:00", "activity": "활동 설명" },
          { "time": "14:00-17:00", "activity": "활동 설명" },
          { "time": "18:00-20:00", "activity": "활동 설명" }
        ],
        "day_2": [ ... ],
        "day_3": [ ... ],
        "day_4": [ ... ],
        "day_5": [ ... ]  // 여행 기간에 맞춰 자동으로 일수 조정 (4박 5일이면 day_5까지)
      }
    }
  ]
}
"""

if __name__ == "__main__":
    print("[INFO] Gemini 여행 추천 API 테스트 실행 중...\n")
    result = generate_travel_recommendation(test_prompt)
    print("\n[Gemini 추천 결과 (파싱된 JSON)]\n")
    pprint(result)
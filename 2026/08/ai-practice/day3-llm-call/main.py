# 프로그램 실행 시작점. 질문을 준비하고 모델 호출 후 답변을 출력
import asyncio
import json

from llm_client import ask_llm, ask_llm_json
from schemas import SummaryResponse
from pydantic import ValidationError

async def main():
    # 모델에 보낼 질문을 준비
    prompt1 = "너를 한국어로 한 문장으로만 소개해줘."

    # 요약할 원본문서다.
    prompt2 = """
    연차 신청 안내

    연차는 사용일 3일 전까지 신청해야 합니다.
    신청은 사내 인사 시스템에서 진행합니다.
    부서장의 승인이 완료되어야 연차를 사용할 수 있습니다.
    긴급한 사유가 있으면 부서장과 먼저 협의해야 합니다.
    """

    # 모델의 응답이 완성될 때까지 대기
    print("모델 응답을 기다리는중...")
    answer = await ask_llm(prompt2)

    # 예제 1: 최종 답변만 출력
    print(answer)

    # 예제 2: 같은 문서를 JSON 형식으로 요약
    print("\nJSON 응답을 기다리는 중...")
    answer2 = await ask_llm_json(prompt2)

    # 모델이 반환된 JSON 문자열을 출력
    print(answer2)

    # JSON 문자열을 Python 딕셔너리로 변환
    result2 = json.loads(answer2)

    # 변환 전후의 자료형을 확인
    print("변환 전:", type(answer2))
    print("변환 후:", type(result2))

    # 딕셔너리에서 제목을 꺼내 출력한다.
    print("문서 제목:", result2["title"])

    # 딕셔너리가 지정한 필드, 타입, 항목 수 조건을 만족하는지 검사
    validated_result2 = SummaryResponse.model_validate(result2)

    # 검증된 객체의 필드에 접근
    print("검증된 제목:", validated_result2.title)
    print("검증된 요약:", validated_result2.summary)

    # 예제 3: 잘못된 모델 응답을 가정
    # summary는 리스트여야 하지만 문자열을 넣었다.
    invalid_result3 = {
        "title": "연차 신청 안내",
        "summary": "연차는 3일 전에 신청합니다.",
    }

    try:
        # 응답이 SummaryResponse의 구조에 맞는지 검사
        validated_result3 = SummaryResponse.model_validate(invalid_result3)
        print("검증 성공:", validated_result3)
    except ValidationError as error:
        # 검증 실패를 잡아 프로그램 종료 대신 오류를 출력한다.
        print("응답 검증 실패:", error)

    # 예제 4: JSON에서 필드 사이의 쉼표가 빠진 응답을 가정
    invalid_json4 = '{"title": "연차 안내" "summary": []}'

    try:
        # JSON 문자열을 딕셔너리로 변환한다.
        result4 = json.loads(invalid_json4)
        print("JSON 변환 성공:", result4)
    except json.JSONDecodeError as error:
        # JSON 문법 오류를 잡아 출력
        print("JSON 변환 실패:", error)
        
# 비동기 main 함수를 실행
asyncio.run(main())

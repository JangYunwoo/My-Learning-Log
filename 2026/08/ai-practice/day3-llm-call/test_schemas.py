import pytest

from pydantic import ValidationError
from schemas import SummaryResponse

def test_summary_response_success():
    # 정상적인 모델 응답을 가정한 데이터
    result = {
        "title": "연차 신청 안내",
        "summary": ["연차는 사용일 3일 전까지 신청해야 합니다."],
    }

    # 응답 구조를 검증
    validated_result = SummaryResponse.model_validate(result)

    # 검증된 객체에 데이터가 올바르게 들어갔는지 확인
    assert validated_result.title == "연차 신청 안내"
    assert validated_result.summary == [
        "연차는 사용일 3일 전까지 신청해야 합니다."
    ]

def test_summary_response_invalid_type():
    # summary는 리스트여야 하지만 문자열을 넣는다.
    result = {
        "title": "연차 신청 안내",
        "summary": "연차는 3일 전에 신청합니다.",
    }

    # ValidationError가 발생해야 테스트가 통과
    with pytest.raises(ValidationError):
        SummaryResponse.model_validate(result)

def test_summary_response_too_many_items():
    # 최대 3개라는 조건을 넘기도록 요약 4개를 넣음
    result = {
        "title": "연차 신청 안내",
        "summary": [
            "연차는 3일 전에 신청합니다.",
            "사내 인사 시스템에서 신청합니다.",
            "부서장의 승인이 필요합니다.",
            "긴급한 경우 사전에 협의합니다.",
        ],
    }

    # Field(max_length=3) 조건 위반으로 예외가 발생
    with pytest.raises(ValidationError):
        SummaryResponse.model_validate(result)
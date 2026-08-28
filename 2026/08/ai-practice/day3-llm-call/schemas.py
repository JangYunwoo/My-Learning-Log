# 데이터가 어떤 구조여야 하는지 정의하는 파일
from pydantic import BaseModel, Field

# 모델이 반환해야 할 요약 결과의 구조를 정의
class SummaryResponse(BaseModel):
    # 문서 제목은 문자열
    title: str

    # 요약은 문자열 리스트, 항목은 최대 3개
    summary: list[str] = Field(max_length=3)
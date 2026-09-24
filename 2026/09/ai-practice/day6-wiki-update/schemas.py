# 저장할 위키 데이터의 구조·검증 조건

from pydantic import BaseModel, Field

# Agent가 생성할 위키 문서의 구조를 정의
class WikiPage(BaseModel):
    # 위키 제목은 빈 문자열일 수 없음
    title: str = Field(min_length=1)

    # 위키 본문도 빈 문자열일 수 없음
    content: str = Field(min_length=1)

    # 작성에 참고한 원본 파일이 하나 이상 있어야함
    source_documents: list[str] = Field(min_length=1)
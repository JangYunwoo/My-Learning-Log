# Pydantic으로 요청, 응답 자료형 정의

from pydantic import BaseModel

class DocumentRequest(BaseModel):
    document_id: int
    title: str
    content: str

# 문서 처리 결과로 응답할 데이터의 형태를 정의
class DocumentResponse(BaseModel):

    # 처리할 문서의 ID
    document_id: int

    # 불필요한 공백을 정리한 문서 내용
    normalized_content: str

    # 정리된 내용의 문자 수
    character_count: int

# 문서 처리 함수
import asyncio
from schemas import DocumentRequest, DocumentResponse

# 요청받은 문서를 처리하고 응답 객체를 반환
async def process_document(document: DocumentRequest) -> DocumentResponse:

    # 공백만 있거나 내용이 없으면 처리 중단
    if not document.content.strip():
        raise ValueError("문서 내용이 비어 있습니다.")

    # 외부 API 응답을 기다리는 상황 흉내
    await asyncio.sleep(1)

    # 연속된 공백과 줄바꿈을 공백 하나로 정의
    normalized_content = " ". join(document.content.split())

    # 처리 결과를 응답 자료형에 담아 반환
    return DocumentResponse(
        document_id=document.document_id,
        normalized_content=normalized_content,
        character_count=len(normalized_content),
    )

# 비동기 처리를 사용하기 위한 기본 라이브러리
import asyncio

# 선언한 클래스를 선언
from models import Document, ProcessResult

# 비동기 함수를 선언, document 변수는 Document 객체를 사용하며 결과는 ProcessResult 객체로 반환한다.
async def process_document(document: Document) -> ProcessResult:

    # 빈 문서를 거부하도록 예외처리
    if not document.content.strip():
        raise ValueError("문서 내용이 비어 있습니다.")

    # 1초 기다림, time.sleep(1)은 프로그램 전체를 멈춘다.
    # 이는 API 응답을 대기하는 상황을 흉내낸 것임.
    await asyncio.sleep(1)

    normalized_content = " ".join(document.content.split())

    return ProcessResult(
        document_id=document.document_id,
        normalized_content=normalized_content,
        character_count=len(normalized_content),
    )
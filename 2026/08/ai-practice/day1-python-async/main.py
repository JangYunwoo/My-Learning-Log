import asyncio

from models import Document
from processor import process_document

async def main():
    # 정상 처리하기
    document1 = Document(
        document_id=1,
        title="휴가 규정",
        content="연차는       3일 전에\n신청합니다.",
    )

    # 비정상 처리하기
    document2 = Document(
        document_id=2,
        title="빈 문서",
        content="    ",
    )

    # 정상 출력하기
    result1 = await process_document(document1)
    print(result1)

    # 비정상 예외처리
    try:
        result2 = await process_document(document2)
        print(result2)
    except ValueError as error:
        print(f"처리 실패: {error}")

    # 동시 처리
    document3 = Document(
        document_id=3,
        title="출장 규정",
        content="출장비는 영수증 제출 후 지급합니다.",
    )

    results = await asyncio.gather(
        process_document(document1),
        process_document(document3),
    )

    print("동시 처리 결과 : ")
    for result in results:
        print(result)

asyncio.run(main())
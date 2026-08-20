# 테스트 모듈
import pytest

from models import Document
from processor import process_document

# 아래의 테스트가 비동기 함수라는 것을 pytest에 알려주는 데코레이터.
# pytest는 이름이 test_로 시작하는 함수를 자동으로 찾아 실행한다.
@pytest.mark.asyncio
async def test_process_document_success():
    document = Document(
        document_id=1,
        title="휴가 규정",
        content="연차는       3일 전에\n신청합니다.",
    )

    result = await process_document(document)

    assert result.document_id == 1
    assert result.normalized_content == "연차는 3일 전에 신청합니다."
    assert result.character_count == 16

# 비정상 내용을 테스트한 경우
@pytest.mark.asyncio
async def test_process_document_empty_content():
    document = Document(
        document_id=2,
        title="빈 문서",
        content="   ",
    )

    # ValueError가 발생하면 테스트를 통과한다.
    with pytest.raises(
        ValueError,
        match="문서 내용이 비어 있습니다.",
    ):
        await process_document(document)
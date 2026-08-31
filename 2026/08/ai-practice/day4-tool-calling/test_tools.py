import pytest

from tools import get_document

# 정상적인 문서 ID로 조회하면 저장된 원문을 반환하는지 확인
def test_get_document_success():
    result = get_document(document_id=1)

    assert result == "연차는 사용일 3일 전까지 신청해야 합니다."

def test_get_documnet_not_fount():
    with pytest.raises(ValueError, match="해당 문서를 찾을 수 없습니다"):
        get_document(document_id=999)
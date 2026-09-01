# 도구 함수 테스트

import pytest
import tools

from tools import search_documents, read_document
from pydantic import ValidationError
from tools import search_documents, read_document, save_wiki

# "연차"가 포함된 문서를 검색하면 leave.txt가 나오는지 확인
def test_search_documents_success():
    result = search_documents(query="연차")

    assert result == ["leave.txt"]

# leave.txt를 읽으면 저장된 문서 내용이 반환되는지 확인
def test_read_document_success():
    result = read_document(file_name="leave.txt")

    assert "제목: 연차 신청 안내" in result
    assert "연차는 사용일 3일 전까지 신청해야 합니다." in result

# 존재하지 않는 파일을 읽으면 ValueError가 발생하는지 확인
def test_read_document_not_found():
    with pytest.raises(
        ValueError,
        match="해당 문서를 찾을 수 없습니다",
    ):
        read_document(file_name="missing.txt")

# 위키 본문이 비어 있으면 Pydantic 검증에서 실패하는지 확인
def test_save_wiki_empty_content():
    with pytest.raises(ValidationError):
        save_wiki(
            file_name="invalid_wiki",
            title="연차 신청 안내",
            content="",
            source_documents=["leave.txt"],
        )

# 실제 wiki 폴더 대신 pytest의 임시 폴더에 위키를 저장해 확인
def test_save_wiki_succestt(tmp_path, monkeypatch):
    # save_wiki()가 사용할 저장 폴더를 임시 폴더로 바꿈
    monkeypatch.setattr(tools, "WIKI_DIR", tmp_path)

    result = tools.save_wiki(
        file_name="test_wiki",
        title="연차 신청 안내",
        content="연차는 사용일 3일 전까지 신청해야 합니다.",
        source_documents=["leave.txt"],
    )

    saved_path = tmp_path / "test_wiki.md"

    # 반환된 파일 이름과 실제 파일 생성을 확인
    assert result == "test_wiki.md"
    assert saved_path.exists()
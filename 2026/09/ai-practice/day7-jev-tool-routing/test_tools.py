# 도구 함수 테스트

import pytest
import tools

from tools import search_documents, read_document
from pydantic import ValidationError
from tools import search_documents, read_document, save_wiki
from types import SimpleNamespace
from agent import execute_tool

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

def test_execute_tool_search():
    tool_call = SimpleNamespace(
        function=SimpleNamespace(
            name="search_documents",
            arguments={"query": "연차"},
        )
    )

    result = execute_tool(tool_call)

    assert "leave.txt" in result

# 임시 폴더에 위키를 준비하고 내용을 그대로 읽는지 확인
def test_read_wiki_success(tmp_path, monkeypatch):
    monkeypatch.setattr(tools, "WIKI_DIR", tmp_path)

    # 테스트용 위키 파일을 만든다.
    wiki_path = tmp_path / "sample.md"
    wiki_path.write_text(
        "# 연차 안내\n\n연차는 3일 전에 신청합니다.",
        encoding="utf-8",
    )

    result = tools.read_wiki(file_name="sample.md")

    assert result == "# 연차 안내\n\n연차는 3일 전에 신청합니다."


# 기존 위키를 수정하면 같은 파일에 새 내용이 저장되는지 확인
def test_update_wiki_success(tmp_path, monkeypatch):
    monkeypatch.setattr(tools, "WIKI_DIR", tmp_path)

    # 수정 전 위키를 준비
    wiki_path = tmp_path / "leave_guide.md"
    wiki_path.write_text(
        "# 연차 안내\n\n기존 본문",
        encoding="utf-8",
    )

    result = tools.update_wiki(
        file_name="leave_guide.md",
        title="연차 신청 안내",
        content="연차는 3일 전에 신청하며, 부서장 승인이 필요합니다.",
        source_documents=["leave.txt"],
    )

    # 같은 파일이 수정됐는지 내용을 확인
    updated_content = wiki_path.read_text(encoding="utf-8")

    assert result == "leave_guide.md"
    assert "부서장 승인이 필요합니다." in updated_content
    assert "기존 본문" not in updated_content
    assert "- leave.txt" in updated_content


# title을 생략하면 기존 위키 제목이 유지되는지 확인
def test_update_wiki_keeps_existing_title(tmp_path, monkeypatch):
    monkeypatch.setattr(tools, "WIKI_DIR", tmp_path)

    wiki_path = tmp_path / "leave_guide.md"
    wiki_path.write_text(
        "# 연차 신청 안내\n\n기존 본문",
        encoding="utf-8",
    )

    tools.update_wiki(
        file_name="leave_guide.md",
        content="부서장의 승인이 필요합니다.",
        source_documents=["leave.txt"],
    )

    updated_content = wiki_path.read_text(encoding="utf-8")

    assert updated_content.startswith("# 연차 신청 안내")
    assert "부서장의 승인이 필요합니다." in updated_content

# 문서 검색·읽기·위키 저장 함수

from pathlib import Path
from schemas import WikiPage

# 현재 tools.py가 있는 폴더를 기준으로 documents 폴더 위치를 만듦
DOCUMENTS_DIR = Path(__file__).parent / "documents"
WIKI_DIR = Path(__file__).parent / "wiki"

# documents 폴더의 문서 중 검색어가 포함된 파일 이름을 반환
def search_documents(query: str) -> list[str]:
    matched_documents = []

    # documents 폴더의 모든 txt 파일을 하나씩 확인
    for document_path in DOCUMENTS_DIR.glob("*.txt"):
        content = document_path.read_text(encoding="utf-8")

        # 검색어가 문서 내용에 있으면 파일 이름을 결과에 추가
        # .name은 경로의 마지막 이름 즉 파일명을 추출
        if query in content:
            matched_documents.append(document_path.name)

    return matched_documents

def read_document(file_name: str) -> str:
    document_path = DOCUMENTS_DIR / file_name

    # 해당 파일이 없으면 예외를 발생
    if not document_path.exists():
        raise ValueError("해당 문서를 찾을 수 없습니다.")

    return document_path.read_text(encoding="utf-8")

# 위키 데이터를 검증한 뒤 Markdown 파일로 저장
def save_wiki(
    file_name: str,
    title: str,
    content: str,
    source_documents: list[str],
) -> str:
    # 저장하기 전에 위키 데이터 구조를 검증
    wiki_page = WikiPage(
        title=title,
        content=content,
        source_documents=source_documents,
    )

    # 확장자를 제외한 파일 이름만 받아 Markdown 파일로 저장
    wiki_path = WIKI_DIR / f"{file_name}.md"

    wiki_content = (
        f"# {wiki_page.title}\n\n"
        f"{wiki_page.content}\n\n"
        "## 참고 문서\n\n"
        + "\n".join(
            f"- {source}" for source in wiki_page.source_documents
        )
    )

    wiki_path.write_text(wiki_content, encoding="utf-8")

    return wiki_path.name

SEARCH_DOCUMENT_TOOL = {
    "type": "function",
    "function": {
        "name": "search_documents",
        "description": "검색어가 포함된 문서의 파일 이름을 찾습니다.",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "문서에서 찾을 검색어",
                },
            },
            "required": ["query"],
        },
    },
}

# 모델에 전달할 문서 읽기 도구 설명이다.
READ_DOCUMENT_TOOL = {
    "type": "function",
    "function": {
        "name": "read_document",
        "description": "파일 이름으로 문서의 전체 내용을 읽습니다.",
        "parameters": {
            "type": "object",
            "properties": {
                "file_name": {
                    "type": "string",
                    "description": "읽을 문서의 파일 이름",
                },
            },
            "required": ["file_name"],
        },
    },
}

# 모델에 전달할 위키 저장 도구 설명이다.
SAVE_WIKI_TOOL = {
    "type": "function",
    "function": {
        "name": "save_wiki",
        "description": "원본 문서를 바탕으로 작성한 위키를 Markdown 파일로 저장합니다.",
        "parameters": {
            "type": "object",
            "properties": {
                "file_name": {
                    "type": "string",
                    "description": "확장자를 제외한 저장 파일 이름",
                },
                "title": {
                    "type": "string",
                    "description": "위키 문서의 제목",
                },
                "content": {
                    "type": "string",
                    "description": "원본 문서를 바탕으로 작성한 위키 본문",
                },
                "source_documents": {
                    "type": "array",
                    "items": {
                        "type": "string",
                    },
                    "description": "작성에 참고한 원본 파일 이름 목록",
                },
            },
            "required": [
                "file_name",
                "title",
                "content",
                "source_documents",
            ],
        },
    },
}
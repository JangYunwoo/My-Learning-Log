# 문서 검색·읽기·위키 저장 함수

from pathlib import Path
from schemas import WikiPage
from copy import deepcopy

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

# wiki 폴더에 저장된 markdown 파일의 내용을 읽는다.
def read_wiki(file_name: str) -> str:
    wiki_path = (WIKI_DIR / file_name).resolve()

    # 지정된 wiki 폴더 밖의 파일에는 접근하지 못하게 한다.
    if not wiki_path.is_relative_to(WIKI_DIR.resolve()):
        raise ValueError("wiki 폴더 안의 파일만 읽을 수 있습니다.")

    # Markdown 파일이 실제로 있는지 확인한다.
    if wiki_path.suffix != ".md" or not wiki_path.is_file():
        raise ValueError("해당 위키 파일을 찾을 수 없습니다.")

    return wiki_path.read_text(encoding="utf-8")

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

# 이미 존재하는 위키를 검증된 새 내용으로 교체
def update_wiki(
        file_name: str,
        content: str,
        source_documents: list[str],
        title: str | None = None,
) -> str:
    # 폴더 경로 없이 파일 이름만 받음
    if Path(file_name).name != file_name:
        raise ValueError("경로 없이 위키 파일 이름만 입력해 주세요.")

    wiki_path = WIKI_DIR / file_name

    # 기존 Markdown 파일이 있어야 수정할 수 있음
    if wiki_path.suffix != ".md" or not wiki_path.is_file():
        raise ValueError("수정할 위키 파일을 찾을 수 없습니다.")

    # title이 생략되면 기존 위키의 제목을 유지
    if title is None:
        current_content = wiki_path.read_text(encoding="utf-8")
        first_line =current_content.splitlines()[0]

        if not first_line.startswith("# "):
            raise ValueError("기존 위키에서 제목을 찾을 수 없습니다.")

        title = first_line.removeprefix("# ").strip()

    # 기존 저장 함수의 데이터 검증과 Markdown 작성 기능을 재사용
    return save_wiki(
        file_name=wiki_path.stem,
        title=title,
        content=content,
        source_documents=source_documents,
    )

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

# 모델에 전달할 기존 위키 읽기 도구 설명이다.
READ_WIKI_TOOL = {
    "type": "function",
    "function": {
        "name": "read_wiki",
        "description": "기존 위키의 내용을 확인합니다. 위키를 수정하기 전에 사용합니다.",
        "parameters": {
            "type": "object",
            "properties": {
                "file_name": {
                    "type": "string",
                    "description": "읽을 위키 파일 이름. .md 확장자를 포함합니다.",
                },
            },
            "required": ["file_name"],
        },
    },
}

# 기존 위키를 수정할 때 모델이 사용할 도구 설명이다.
UPDATE_WIKI_TOOL = {
    "type": "function",
    "function": {
        "name": "update_wiki",
        "description": (
            "기존 위키를 수정합니다. 먼저 read_wiki로 현재 내용을 읽고, "
            "유지할 내용과 수정 사항을 합친 전체 본문을 전달합니다."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "file_name": {
                    "type": "string",
                    "description": "수정할 기존 위키 파일 이름. .md 확장자를 포함합니다.",
                },
                "title": {
                    "type": "string",
                    "description": "수정 후 위키 제목",
                },
                "content": {
                    "type": "string",
                    "description": "유지할 내용과 수정 사항을 모두 포함한 전체 본문",
                },
                "source_documents": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "수정 후 위키 내용의 근거가 되는 원본 파일 이름 목록",
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

UPDATE_WIKI_TOOL2 = deepcopy(UPDATE_WIKI_TOOL)

UPDATE_WIKI_TOOL2["function"]["description"] = (
    "기존 위키를 수정합니다. content에는 제목과 참고 문서를 제외한"
    "수정 후 전체 본문만 전달합니다."
)

UPDATE_WIKI_TOOL2["function"]["parameters"]["properties"]["content"]["description"] = (
    "수정 후 전체 본문. '# 제목'과 '## 참고 문서'는 포함하지 않습니다."
)

# title을 생략하면 기존 위키 제목을 유지
UPDATE_WIKI_TOOL2["function"]["parameters"]["properties"]["title"]["description"] = (
    "수정 후 위키 제목. 생략하면 기존 제목을 유지합니다."
)

UPDATE_WIKI_TOOL2["function"]["parameters"]["required"].remove("title")
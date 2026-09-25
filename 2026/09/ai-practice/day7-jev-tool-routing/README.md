# 6일차: Wiki Update Agent

## 학습 목표

5일차에 만든 Wiki Agent를 확장하여 기존 위키를 읽고, 원본문서를 확인한 뒤 내용을 수정하는 Agent를 구현한다. 또한 여러 `if` 문으로 도구를 선택하던 코드를 딕셔너리 기반 도구 레지스트리로 변경한다.

## 주요 학습 내용

- 딕셔너리를 사용한 도구 함수 관리
- 기존 Markdown 위키 읽기
- 기존 위키 내용 수정 및 덮어쓰기
- LLM의 도구 호출 결과를 반복해서 처리하는 Agent 루프
- 누락된 도구 인자를 안전하게 처리하는 방법
- `tmp_path`와 `monkeypatch`를 활용한 파일 테스트

## 폴더와 파일

| 이름 | 역할 |
| --- | --- |
| `documents/` | Agent가 참고하는 원본문서를 보관한다. |
| `wiki/` | 생성하거나 수정한 Markdown 위키를 보관한다. |
| `agent.py` | 도구 레지스트리, LLM 호출, Agent 반복 실행을 담당한다. |
| `tools.py` | 문서 및 위키를 검색·읽기·저장·수정하는 함수를 정의한다. |
| `prompts.py` | 위키 수정 Agent가 따라야 할 작업 순서를 정의한다. |
| `schemas.py` | 위키 제목, 본문, 참고 문서의 데이터 구조를 검증한다. |
| `update_main.py` | Wiki Update Agent를 실행하는 진입점이다. |
| `test_tools.py` | 도구 함수의 정상 동작과 오류 상황을 검사한다. |

## 딕셔너리 기반 도구 실행

기존에는 도구 이름을 여러 `if` 문으로 비교하여 실행할 함수를 선택했다. 6일차에는 도구 이름과 Python 함수를 딕셔너리로 연결했다.

```python
TOOL_FUNCTIONS = {
    "search_documents": search_documents,
    "read_document": read_document,
    "save_wiki": save_wiki,
    "read_wiki": read_wiki,
    "update_wiki": update_wiki,
}
```

`execute_tool()`은 모델이 요청한 함수 이름으로 딕셔너리를 조회하고, 전달받은 인자를 풀어서 함수를 실행한다.

```python
def execute_tool(tool_call):
    function_name = tool_call.function.name
    arguments = tool_call.function.arguments
    tool_function = TOOL_FUNCTIONS.get(function_name)

    if tool_function is None:
        raise ValueError(f"지원하지 않는 도구입니다: {function_name}")

    return tool_function(**arguments)
```

`**arguments`는 딕셔너리에 들어 있는 값을 함수의 키워드 인자로 전달한다.

## 위키 읽기

`read_wiki()`는 `wiki` 폴더 안의 Markdown 파일을 읽어 문자열로 반환한다.

- `.md` 파일만 읽는다.
- 존재하지 않는 파일은 `ValueError`로 처리한다.
- `wiki` 폴더 밖의 파일을 읽지 못하도록 경로를 검사한다.

## 위키 수정

`update_wiki()`는 기존 위키 파일이 존재하는지 확인한 후 `save_wiki()`를 재사용하여 같은 파일에 수정된 내용을 저장한다.

```python
def update_wiki(
    file_name: str,
    content: str,
    source_documents: list[str],
    title: str | None = None,
) -> str:
    ...
```

`title: str | None`은 제목으로 문자열 또는 `None`을 받을 수 있다는 뜻이다. 모델이 `title`을 생략하면 기존 Markdown 파일의 첫 번째 줄에서 제목을 읽어 그대로 유지한다.

```text
title 전달됨 → 전달된 제목 사용
title 생략됨 → 기존 위키 제목 유지
```

`content`에는 본문만 전달한다. 제목과 참고 문서는 `save_wiki()`가 별도로 작성하므로 본문에 다시 포함하면 내용이 중복된다.

## 도구 설명 보완

기존 도구 설명은 모델이 제목과 참고 문서까지 `content`에 포함할 여지가 있었다. 새 도구 설명에서는 다음 규칙을 명시했다.

- `content`에는 수정 후 전체 본문만 전달한다.
- `# 제목`과 `## 참고 문서`는 `content`에 포함하지 않는다.
- `title`을 생략하면 기존 제목을 유지한다.

기존 도구 정의를 보존하기 위해 `deepcopy()`로 복사한 뒤 설명을 수정했다. 중첩 딕셔너리를 복사할 때 `deepcopy()`를 사용하면 새 딕셔너리의 내부 값을 변경해도 기존 딕셔너리에 영향을 주지 않는다.

## Wiki Update Agent 흐름

```text
1. read_wiki로 현재 위키를 읽는다.
2. read_document로 참고 원문을 확인한다.
3. 기존 내용과 원문을 바탕으로 수정된 본문을 작성한다.
4. update_wiki로 기존 파일을 수정한다.
5. 도구 호출이 없으면 최종 답변을 반환하고 종료한다.
```

실행 중 확인한 결과:

```text
Wiki Update Agent 단계 1: read_wiki
Wiki Update Agent 단계 2: read_document
Wiki Update Agent 단계 3: update_wiki
Wiki Update Agent 단계 4: 최종 답변
```

수정 결과 `leave_guide.md`에는 부서장 승인 조건과 긴급한 경우의 처리 방법이 추가됐다.

## 프롬프트와 도구 호출

작은 로컬 모델은 도구를 호출해야 할 상황에서도 함수 호출 내용을 일반 JSON 문자열로 답할 수 있다. 이를 방지하기 위해 시스템 프롬프트에 다음 규칙을 명시했다.

- 도구 호출 내용을 일반 답변이나 JSON 문자열로 출력하지 않는다.
- 반드시 `tool_calls`로 도구를 호출한다.
- `update_wiki` 실행 전에는 최종 답변을 작성하지 않는다.
- 기존 위키와 원본문서를 모두 읽은 뒤 수정한다.

프롬프트와 도구 설명을 명확히 작성하더라도 모델이 필수 인자를 누락할 수 있으므로 Python 함수에서도 안전하게 처리해야 한다.

## 테스트에서 임시 폴더 사용

파일 저장과 수정 테스트가 실제 `wiki` 폴더를 변경하지 않도록 pytest의 `tmp_path`와 `monkeypatch`를 사용했다.

```python
def test_example(tmp_path, monkeypatch):
    monkeypatch.setattr(tools, "WIKI_DIR", tmp_path)
```

- `tmp_path`: pytest가 테스트마다 만들어 주는 임시 폴더다.
- `monkeypatch`: 테스트 중에만 객체의 값이나 함수를 임시로 변경한다.
- `monkeypatch.setattr(tools, "WIKI_DIR", tmp_path)`: `tools.py`의 저장 위치를 테스트용 임시 폴더로 바꾼다.
- 테스트가 끝나면 `WIKI_DIR`은 원래 값으로 자동 복구된다.

`monkeypatch`와 `tmp_path`는 테스트 함수의 매개변수 이름을 보고 pytest가 자동으로 전달하는 fixture다.

## 테스트

전체 테스트 실행:

```bash
python -m pytest -v
```

학습 중 실행 결과:

```text
9 passed
```

추가로 확인한 주요 내용:

- 딕셔너리에서 검색 도구를 찾아 실행하는지
- 기존 위키를 정상적으로 읽는지
- 같은 파일에 수정된 위키가 저장되는지
- `title`을 생략해도 기존 제목이 유지되는지
- 테스트 파일이 실제 `wiki` 폴더가 아닌 임시 폴더에 저장되는지

## 실행 방법

Git Bash에서 `ai-practice` 폴더의 가상환경을 활성화하고 6일차 폴더로 이동한다.

```bash
source venv/Scripts/activate
cd day6-wiki-update
python update_main.py
```

Agent를 실행하려면 Ollama가 실행 중이고 `qwen3:4b` 모델이 설치되어 있어야 한다.

```bash
ollama list
```

## 정리

- LLM은 현재 대화 기록과 도구 설명을 보고 다음 도구를 선택한다.
- Python은 허용된 도구를 딕셔너리에서 찾아 실제로 실행한다.
- 위키 수정 전에는 기존 위키와 원본문서를 모두 확인한다.
- 모델의 출력은 항상 완전하다고 가정하지 않고 Python 코드에서 누락된 값을 보완한다.
- 파일 관련 테스트는 임시 폴더를 사용해 실제 학습 데이터를 보호한다.

6일차의 핵심 결과는 기존 위키를 읽고 원본문서의 근거를 확인한 뒤, 내용을 유지·보완하여 같은 Markdown 파일에 다시 저장하는 Wiki Update Agent를 구현한 것이다.

# 5일차: Mini Wiki Agent

## 학습 목표

로컬 LLM이 현재 작업 기록을 보고 다음 도구를 선택하도록 만들고, 문서 검색 → 읽기 → 위키 저장 → 최종 답변까지 반복하는 Agent 루프를 구현한다.

## 사용한 라이브러리와 도구

| 이름 | 역할 |
| --- | --- |
| Ollama | 로컬에서 모델을 실행하고 채팅 API를 제공한다. |
| Qwen3:4b | 작업 기록과 도구 설명을 보고 다음 행동을 선택한다. |
| `ollama.AsyncClient` | Ollama 서버에 비동기 요청을 보낸다. |
| `pathlib.Path` | 문서와 위키 파일의 경로를 만들고 파일을 읽고 쓴다. |
| Pydantic | 저장할 위키 데이터의 필드와 최소 길이를 검증한다. |
| pytest | 도구 함수를 모델과 분리해서 자동으로 검사한다. |

## 폴더와 파일

| 이름 | 역할 |
| --- | --- |
| `documents/` | Agent가 조사할 원본 문서를 보관한다. |
| `wiki/` | 생성한 Markdown 위키를 저장한다. |
| `main.py` | 단계별 예제와 완성된 Agent를 실행한다. |
| `agent.py` | 모델 호출, 도구 실행, 결과 기록, 반복을 담당한다. |
| `tools.py` | 검색·읽기·저장 함수와 도구 설명을 정의한다. |
| `prompts.py` | 조사 Agent와 Wiki Agent의 작업 규칙을 정의한다. |
| `schemas.py` | 저장할 `WikiPage` 구조를 정의한다. |
| `test_tools.py` | 도구 함수의 정상 동작과 오류를 검사한다. |

원본 문서는 `leave.txt`와 `business_trip.txt` 두 개를 사용했다.

## 문서 검색과 읽기

```python
def search_documents(query: str) -> list[str]:
    ...

def read_document(file_name: str) -> str:
    ...
```

- `search_documents()`는 `documents` 폴더의 `.txt` 파일을 읽고 검색어가 포함된 파일 이름 목록을 반환한다.
- `read_document()`는 파일 이름을 받아 원문 전체를 반환한다.
- 없는 파일을 읽으면 `ValueError`가 발생한다.
- `Path(__file__).parent`를 기준으로 경로를 만들기 때문에 코드 파일 주변의 폴더를 찾을 수 있다.
- `document_path.name`은 전체 경로에서 마지막 파일 이름만 꺼내는 `Path` 속성이다.

## 도구 설명

모델에는 Python 함수 자체가 아니라 JSON Schema 형태의 설명을 전달했다.

| 도구 | 주요 인자 | 반환값 |
| --- | --- | --- |
| `search_documents` | `query: str` | 파일 이름 목록 `list[str]` |
| `read_document` | `file_name: str` | 문서 원문 `str` |
| `save_wiki` | 파일 이름·제목·본문·출처 목록 | 저장된 파일 이름 `str` |

`tools=[...]`는 모델에게 사용 가능한 선택지를 알려준다. `client.chat()` 자체가 판단하는 것이 아니라 Qwen이 메시지 기록과 도구 설명을 보고 일반 답변 또는 `tool_calls`를 생성한다. Python은 모델이 요청한 함수를 실제로 실행한다.

## 고정 흐름에서 Agent 루프로

처음에는 각 단계를 별도 함수로 직접 연결했다.

```text
request_first_tool()
→ request_next_tool()
→ request_final_answer()
```

이후 `request_agent_step(messages)`와 `run_agent()`를 만들었다. Agent는 매 단계마다 지금까지의 전체 기록을 보고 다음 행동을 선택한다.

```text
도구가 필요함 → tool_calls 반환 → Python이 실행 → 결과를 messages에 추가
도구가 필요 없음 → 일반 content 반환 → Agent 루프 종료
```

```python
if not agent_message.tool_calls:
    return agent_message.content
```

`tool_result`에는 현재 실행한 도구 하나의 반환값이 들어간다. 검색 결과는 리스트일 수 있고 읽기·저장 결과는 문자열이다. 메시지의 `content`로 보내기 위해 `str(tool_result)`로 문자열화하며, 원래 변수의 자료형은 바뀌지 않는다.

각 도구 결과는 바로 `messages`에 추가되므로 이전 단계의 기록은 누적된다.

## 위키 데이터 검증과 저장

```python
class WikiPage(BaseModel):
    title: str = Field(min_length=1)
    content: str = Field(min_length=1)
    source_documents: list[str] = Field(min_length=1)
```

- 제목과 본문은 최소 한 글자여야 한다.
- 참고 원본 파일은 최소 하나 있어야 한다.
- 현재 조건에서는 공백 한 칸도 길이 1이므로 통과한다.

`save_wiki()`는 데이터를 `WikiPage`로 검증하고 Markdown 문자열을 만든 뒤 `wiki` 폴더에 저장한다.

```markdown
# 위키 제목

위키 본문

## 참고 문서

- leave.txt
```

`main.py`의 예제 10은 모델 없이 `save_wiki()`를 직접 호출해 `leave_guide.md`를 만든다. 완성된 Wiki Agent가 만든 파일은 `연차_신청_안내.md`다.

## Wiki Agent 흐름

`WIKI_SYSTEM_PROMPT`에는 검색 → 읽기 → 위키 작성·저장 → 파일 이름 안내 순서를 작성했다. `run_wiki_agent()`는 최대 8단계 동안 모델의 선택을 반복한다. 최대 횟수는 무한 반복을 방지한다.

실습에서 확인한 흐름:

```text
Wiki Agent 단계 1: search_documents(query="연차")
→ ['leave.txt']

Wiki Agent 단계 2: read_document(file_name="leave.txt")
→ 연차 문서 원문

Wiki Agent 단계 3: save_wiki(...)
→ 연차_신청_안내.md

Wiki Agent 단계 4: tool_calls 없음
→ 파일 이름을 최종 답변으로 반환하고 종료
```

파일 이름이 두 번 보이는 이유는 첫 번째가 Python 저장 함수의 실행 로그이고, 두 번째가 저장 결과를 본 Qwen의 사용자용 최종 답변이기 때문이다. 파일이 두 번 저장된 것은 아니다.

## 테스트

```bash
python -m pytest test_tools.py -v
```

| 테스트 | 검사 내용 |
| --- | --- |
| 검색 성공 | `연차` 검색 결과가 `leave.txt`인지 |
| 읽기 성공 | 원문에 제목과 신청 기한이 포함되는지 |
| 읽기 실패 | 없는 파일에서 `ValueError`가 발생하는지 |
| 검증 실패 | 빈 본문에서 `ValidationError`가 발생하는지 |
| 저장 성공 | 임시 폴더에 Markdown 파일이 생성되는지 |

학습 중 실행 결과: **5 passed**.

- `tmp_path`: pytest가 제공하는 테스트용 임시 폴더.
- `monkeypatch`: 테스트 중에만 `tools.WIKI_DIR`을 임시 폴더로 교체하고 종료 후 복구한다.

따라서 실제 `wiki` 폴더에는 테스트 파일이 남지 않는다. 테스트는 모델을 호출하지 않으므로 Ollama가 실행 중이지 않아도 된다.

## 실행 방법

Git Bash에서 `ai-practice` 폴더 기준:

```bash
source venv/Scripts/activate
cd day5-wiki-agent
python main.py
```

Agent 예제를 실행하려면 Ollama가 실행 중이고 `qwen3:4b` 모델이 준비되어 있어야 한다.

```bash
ollama list
```

`main.py`에는 학습 과정을 남기기 위해 직접 호출, 고정 흐름, 일반 Agent 루프, Wiki Agent 루프가 모두 들어 있다. 따라서 한 번 실행하면 여러 모델 호출과 파일 저장 예제가 순서대로 실행된다.

## 현재 구현의 범위

- 검색은 벡터 검색이 아니라 단순 문자열 포함 검사다.
- 도구 결과는 Python 표현을 `str()`로 바꿔 전달하며 엄격한 JSON 직렬화는 사용하지 않았다.
- Agent 루프 안에서 도구 실행 예외를 복구해 모델에 알려주는 처리는 아직 없다.
- 파일 이름의 경로 문자와 기존 파일 덮어쓰기를 제한하는 검증은 아직 없다.
- 모델의 도구 선택이 항상 옳다고 가정하지 않고 반복 횟수를 제한했다.
- 테스트는 도구 함수에 집중하며 실제 모델의 비결정적 선택은 자동 테스트하지 않는다.

## 정리

- Qwen: 기록과 프롬프트를 보고 다음 도구 또는 최종 답변을 선택한다.
- Python: 허용된 도구를 실행하고 결과, 기록, 반복 횟수를 관리한다.
- Ollama의 `chat()`: 메시지와 도구 설명을 모델에 전달하고 응답을 받아온다.

핵심 결과는 모델이 검색 → 읽기 → 저장을 스스로 이어 가고, 도구 호출이 없어지면 Python이 최종 답변으로 판단해 종료하는 반복 구조다.

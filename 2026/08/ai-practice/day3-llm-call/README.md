# 3일차: 로컬 LLM 호출과 응답 검증

## 학습 목표

Python에서 로컬 LLM으로 문서를 요약하고, JSON 응답을 변환·검증하여 프로그램에서 사용할 수 있도록 만든다.

## 사용한 라이브러리와 도구

| 이름 | 역할 |
| --- | --- |
| Ollama 프로그램 | 로컬에서 모델을 실행하고 API를 제공한다. |
| Qwen3:4b | 문서를 읽고 요약을 생성하는 모델이다. |
| `ollama.AsyncClient` | Ollama 서버에 비동기로 요청한다. |
| `asyncio` | 비동기 함수를 실행하는 Python 기본 모듈이다. |
| `json` | JSON 문자열을 Python 데이터로 변환하는 기본 모듈이다. |
| `pydantic` | 응답의 필드, 자료형, 항목 수를 검증한다. |
| `pytest` | 검증 코드가 예상대로 동작하는지 자동으로 확인한다. |

## 파일별 역할

| 파일 | 역할 |
| --- | --- |
| `main.py` | 문서를 준비하고 모델 호출, 응답 변환·검증, 오류 예제를 실행한다. |
| `llm_client.py` | `ask_llm()`과 `ask_llm_json()`으로 모델을 호출한다. |
| `prompts.py` | 일반 요약과 JSON 요약에 사용할 시스템 지시문을 정의한다. |
| `schemas.py` | 요약 결과의 구조인 `SummaryResponse`를 정의한다. |
| `test_schemas.py` | 응답 구조 검증에 대한 테스트 3개를 작성한다. |

## 실습 흐름

```text
문서(prompt2) + 시스템 지시문
→ AsyncClient.chat()으로 Qwen 호출
→ 최종 답변을 문자열로 받기
→ JSON 응답을 json.loads()로 딕셔너리로 변환
→ SummaryResponse.model_validate()로 구조 검증
→ 검증된 객체의 title과 summary 사용
```

### 1. 일반 텍스트 요약

- `SYSTEM_PROMPT`에 문서 요약 역할과 규칙을 작성했다.
- `messages`의 `system`에는 지시문, `user`에는 원본 문서를 넣었다.
- `await ask_llm(prompt2)`로 응답을 기다리고 출력했다.
- `prompt1`은 첫 소개 질문의 기록으로 남겼다. 현재 호출에는 `prompt2`를 사용한다.

### 2. JSON 형식 요약

- 기존 함수를 유지하고 `ask_llm_json()`을 추가했다.
- `JSON_SYSTEM_PROMPT`에 `title`, `summary` 구조를 요청했다.
- `format="json"`을 지정했다. JSON 형식 지정과 필드·자료형 검증은 별개다.
- 반환값은 문자열이므로 `json.loads(answer2)`로 딕셔너리로 변환했다.
- `result2["title"]`로 제목을 꺼냈다.

일반 요약과 JSON 요약은 같은 문서를 보내는 별도의 호출이다. 이전 답변을 다음 요청에 전달하지 않으며, 표현은 같거나 다를 수 있다.

### 3. Pydantic으로 구조 검증

```python
class SummaryResponse(BaseModel):
    title: str
    summary: list[str] = Field(max_length=3)
```

- `title`: 문자열 제목.
- `summary`: 문자열 리스트이며 최대 3개 항목.
- `SummaryResponse.model_validate(result2)`: 딕셔너리를 검증하고 객체를 반환한다.
- 검증 후 `validated_result2.title`, `validated_result2.summary`로 접근한다.

이 검증은 데이터 구조를 검사한다. 요약 내용의 사실 여부까지 보장하지는 않는다. 최소 항목 수 조건이 없으므로 빈 리스트도 허용한다.

### 4. 잘못된 응답 처리

| 예제 | 잘못된 내용 | 발생하는 예외 |
| --- | --- | --- |
| `invalid_result3` | summary에 리스트 대신 문자열을 넣음 | `ValidationError` |
| `invalid_json4` | JSON 필드 사이 쉼표가 빠짐 | `json.JSONDecodeError` |

`try`에서 실행하고 `except`에서 해당 예외를 잡아 오류를 출력했다.

현재 예외 처리는 의도적으로 잘못 만든 예제 3·4에 적용했다. 실제 모델 응답인 `answer2`의 변환·검증은 아직 `try/except`로 감싸지 않았다.

## 모델 호출 옵션

- `think=True`: 모델의 생각 기능을 사용한다.
- `stream=False`: 조각별로 받지 않고 응답이 완성된 뒤 한 번에 받는다. 생각을 끄는 옵션이 아니다.
- `response.message.content`: 최종 답변을 꺼낸다. 생각용 필드는 출력하지 않는다.

실습에서는 생각 끄기를 시도했으나 생각 텍스트가 답변에 섞여 나왔다. 이후 생각을 켜고 최종 답변만 출력하는 방식으로 진행했다.

## 실행 방법

Git Bash에서 `ai-practice` 폴더 기준:

```bash
source venv/Scripts/activate
cd day3-llm-call
python main.py
```

Ollama가 실행 중이고 `qwen3:4b` 모델이 준비되어 있어야 한다. 연결 주소는 `http://localhost:11434`다.

환경을 새로 준비하는 경우에만 다음을 실행한다. Ollama 프로그램은 별도로 설치한다.

```bash
python -m pip install ollama pydantic pytest
ollama pull qwen3:4b
```

실행하면 일반 요약, JSON 요약, 변환 전후 자료형, 검증된 제목·요약, 의도적으로 만든 오류 메시지를 확인할 수 있다. 요약 문장은 실행마다 달라질 수 있다.

## 자동 테스트

`day3-llm-call` 폴더에서 실행한다.

```bash
python -m pytest test_schemas.py -v
```

| 테스트 | 확인 내용 |
| --- | --- |
| `test_summary_response_success` | 정상 데이터의 검증과 필드 값 |
| `test_summary_response_invalid_type` | 문자열 summary를 거부하는지 |
| `test_summary_response_too_many_items` | 요약 항목 4개를 거부하는지 |

실습에서 3개 테스트가 모두 통과했다. 고정 데이터를 사용하는 테스트이므로 모델을 호출하지 않으며 Ollama 실행도 필요하지 않다.

```python
# 이 블록에서 ValidationError가 발생해야 테스트가 통과한다.
with pytest.raises(ValidationError):
    SummaryResponse.model_validate(result)
```

- `raise`: 코드에서 직접 예외를 발생시킨다.
- `pytest.raises(...)`: 지정한 예외가 발생하는지 검사한다. 예외를 만들어 내는 기능이 아니다.
- 예상한 예외가 발생하지 않거나 다른 종류의 예외가 발생하면 테스트가 실패한다.

## 배운 점과 다음 단계

LLM 응답을 출력하는 것과 프로그램에서 사용하는 것은 다르다. JSON 변환과 구조 검증을 구분하고, 잘못된 응답을 거부하는 동작까지 테스트했다.

4일차에는 LLM이 사용할 함수를 선택하고 Python이 실제로 실행하는 Tool Calling을 학습한다.

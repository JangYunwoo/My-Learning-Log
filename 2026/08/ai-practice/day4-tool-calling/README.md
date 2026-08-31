# 4일차: Tool Calling

## 학습 목표

모델이 함수 이름과 인자를 선택하면 Python에서 실제 함수를 실행하고, 그 결과를 모델에 보내 최종 답변을 만드는 흐름을 구현한다.

## 파일과 라이브러리

| 파일 | 역할 |
| --- | --- |
| `tools.py` | 실습 문서, 문서 조회 함수, 모델에 전달할 도구 설명을 정의한다. |
| `llm_client.py` | 도구 선택 요청과 실행 결과 기반 답변 요청을 담당한다. |
| `main.py` | 예제를 실행하고 모델의 요청을 실제 함수 실행으로 연결한다. |
| `test_tools.py` | 문서 조회 함수의 정상 동작과 예외를 검사한다. |

- `ollama.AsyncClient`: 로컬 Ollama 서버에 비동기로 요청한다.
- `asyncio`: Python 기본 모듈. `asyncio.run(main())`으로 비동기 실행을 시작한다.
- `pytest`: 모델 호출 없이 도구 함수 자체를 테스트한다.
- Ollama와 `qwen3:4b`: 3일차에 준비한 로컬 실행 환경과 모델을 그대로 사용한다.

## 1. 문서 조회 함수

`DOCUMENTS`에는 문서 ID를 키로, 원문 문자열을 값으로 저장했다.

```python
def get_document(document_id: int) -> str:
    if document_id not in DOCUMENTS:
        raise ValueError("해당 문서를 찾을 수 없습니다.")

    return DOCUMENTS[document_id]
```

이 함수는 LLM을 사용하지 않는다. 저장된 문자열을 그대로 반환한다.

`DOCUMENTS`처럼 대문자로 작성한 이름은 고정해서 사용할 값이라는 관례다. Python이 수정을 막아 주는 것은 아니다.

## 2. 모델에 도구 설명 전달

`DOCUMENT_TOOL`은 함수 자체가 아니라 모델에 알려줄 설명이다.

| 항목 | 의미 |
| --- | --- |
| `name` | 호출할 함수 이름인 `get_document` |
| `description` | 문서 ID로 문서를 조회하는 도구라는 설명 |
| `parameters` | 함수 인자의 구조 |
| `properties` | `document_id`의 이름과 정수 자료형 설명 |
| `required` | 반드시 전달해야 하는 인자인 `document_id` |

`request_tool()`에서 질문과 도구 설명을 보낸다.

```python
response = await client.chat(
    model="qwen3:4b",
    messages=[{"role": "user", "content": prompt}],
    tools=[DOCUMENT_TOOL],
    think=True,
    stream=False,
)
return response.message
```

이 요청에는 실제 문서 원문이나 함수 구현 코드가 들어가지 않는다. 도구 설명을 보내는 것만으로 함수가 자동 실행되지도 않는다.

## 3. 모델의 요청을 Python에서 실행

현재 첫 번째 질문은 `prompt4`다.

```python
prompt4 = "1번 문서의 내용을 조회해줘."
message4 = await request_tool(prompt4)
```

모델이 도구 호출을 요청하면 다음 정보가 `message4.tool_calls`에 들어온다.

```text
함수 이름: get_document
전달할 인자: {'document_id': 1}
```

`message4`는 직접 정한 변수 이름이고, `tool_calls`는 Ollama 라이브러리가 제공하는 메시지 속성이다.

```python
tool_call4 = message4.tool_calls[0]
function_name4 = tool_call4.function.name
arguments4 = tool_call4.function.arguments
```

요청한 함수 이름이 허용한 `get_document`인지 확인한 뒤 실행한다.

```python
tool_result4 = get_document(**arguments4)
```

`**`는 딕셔너리를 키워드 인자로 풀어 준다.

```python
# arguments4가 {"document_id": 1}이면 아래 두 호출은 같은 의미다.
get_document(**arguments4)
get_document(document_id=1)
```

바깥쪽 `if/else`는 도구 호출 요청이 있는지, 안쪽 `if/else`는 지원하는 함수인지 구분한다.

## 4. 실행 결과를 모델에 전달

`get_document()`가 원문을 그대로 가져오는 함수라면, `answer_with_tool_result()`는 그 원문과 지시를 모델에 보내 답변을 생성하는 함수다. 원본 문서를 수정하는 것은 아니다.

현재 코드는 두 번째 요청에 별도의 `prompt5`를 사용한다.

```python
prompt5 = "문서 번호를 언급하고 이를 바탕으로 신청 기한을 판단해줘"
answer4 = await answer_with_tool_result(
    prompt=prompt5,
    tool_message=message4,
    tool_result=tool_result4,
)
```

함수 안에서 다음 세 항목을 모델에 보낸다.

1. `user`: 답변 작성 지시인 `prompt5`.
2. `assistant`: 앞서 모델이 보냈던 도구 호출 요청인 `message4`.
3. `tool`: Python이 조회한 문서 원문인 `tool_result4`.

문서 번호는 호출 요청의 인자에, 신청 기한은 조회한 문서 원문에 들어 있다. 모델이 이 정보를 참고해 답변한다.

```text
도구 실행 결과: 연차는 사용일 3일 전까지 신청해야 합니다.
최종 답변: 1번 문서에 따르면, 연차 신청 기한은 사용일 3일 전까지입니다.
```

답변 문구는 실행마다 달라질 수 있다. 현재 지시에는 구체적인 신청일과 사용일이 없으므로 특정 신청의 기한 준수 여부가 아니라 규정상의 기한을 설명한다.

코드의 주석에는 두 번째 요청을 '사용자가 처음 보낸 질문'이라고 적어 두었지만, 현재 실제 값은 최초 조회 질문인 `prompt4`가 아니라 후속 지시인 `prompt5`다. 원래 질문을 그대로 전달하는 구성과 구분한다.

### 왜 모델에 다시 보내는가?

Python이 조회한 결과를 모델은 자동으로 알지 못한다. 조회 결과를 이용해 요약, 정보 추출, 조건 판단 등을 시키려면 모델에 전달해야 한다.

원문을 그대로 보여주는 기능만 필요하면 `get_document()`의 반환값을 출력하고 끝내도 된다. 두 번째 호출은 추가 시간이 들고 모델의 해석 오류 가능성도 있으므로 항상 필요한 것은 아니다.

## 5. 없는 문서의 예외 처리

```python
try:
    tool_result4 = get_document(**arguments4)
except ValueError as error:
    print("도구 실행 실패:", error)
    return
```

없는 문서라면 오류를 출력하고 `main()`을 종료한다. 실패 결과를 모델에 전달하거나 최종 답변을 요청하지 않는다.

`prompt6`에는 999번 문서를 요청하는 실습 질문을 남겨 두었다. 현재 호출은 다시 `request_tool(prompt4)`로 되어 있으므로 정상 조회를 실행한다. 오류 흐름을 재확인하려면 호출 인자를 `prompt6`로 선택한다.

실습에서 확인한 실패 출력:

```text
함수 이름: get_document
전달할 인자: {'document_id': 999}
도구 실행 실패: 해당 문서를 찾을 수 없습니다.
```

## 6. 도구 함수 테스트

모델과 분리해 문서 조회 함수만 검사한다.

| 테스트 | 검사 내용 |
| --- | --- |
| 정상 조회 | 1번 문서의 원문이 반환되는지 |
| 없는 문서 조회 | 999번 문서 요청에서 ValueError와 예상 메시지가 발생하는지 |

```python
with pytest.raises(ValueError, match="해당 문서를 찾을 수 없습니다"):
    get_document(document_id=999)
```

직관적으로는 '이 함수를 실행했을 때 ValueError가 발생하고, 메시지도 해당 패턴과 맞아야 한다'는 뜻이다.

- `raise`: 실제 예외를 발생시킨다.
- `pytest.raises`: 예상한 예외가 발생하는지 검사한다.
- `match`: 오류 메시지를 반환하는 것이 아니라 정규식으로 검사한다.
- `with`: 블록의 진입·종료 처리를 맡긴다. 여기서는 `pytest.raises`가 예외를 확인한다.
- 다른 종류의 예외가 발생하거나, 메시지가 일치하지 않거나, 예외가 아예 없으면 실패한다.

## 실행과 확인

Git Bash에서 `ai-practice` 폴더 기준:

```bash
source venv/Scripts/activate
cd day4-tool-calling
python main.py
```

모델을 호출하려면 Ollama가 실행 중이어야 한다. `ollama list`로 서버 응답과 모델 목록을 확인할 수 있다. 연결 주소는 `http://localhost:11434`다.

테스트는 같은 폴더에서 실행한다.

```bash
python -m pytest test_tools.py -v
```

학습 중 실행 결과: **2 passed**. 테스트는 모델을 호출하지 않으므로 Ollama가 실행 중이지 않아도 된다.

## 현재 범위

- 첫 번째 도구 호출 한 건만 처리한다.
- 허용한 도구는 `get_document` 하나다.
- 없는 문서의 `ValueError`를 처리한다. 잘못된 인자의 모든 자료형이나 연결 오류까지 처리하는 코드는 아니다.
- 여러 번 도구를 선택하며 반복하는 Agent 루프는 아직 구현하지 않았다.

모델의 도구 선택 → Python 실행 → 실행 결과 전달 → 최종 답변 생성까지 연결한 것이 이번 실습의 핵심이다.

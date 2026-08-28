# Day 2 - FastAPI 문서 처리 API

## 학습 목표

1일차의 비동기 문서 처리 함수를 HTTP API로 제공한다.
입력을 검증하고, 처리 결과와 오류를 HTTP 응답으로 반환한 뒤 자동 테스트로 확인한다.

## 사용 라이브러리

| 라이브러리 | 역할 |
| --- | --- |
| FastAPI | API 경로 등록과 HTTP 요청·응답 처리 |
| Uvicorn | FastAPI 앱을 실행하는 ASGI 서버 |
| Pydantic | 요청 자료형 검증과 처리 결과 객체 정의 |
| HTTPX | 설치된 TestClient 구현에서 사용하는 HTTP 클라이언트 의존성 |
| pytest | API 자동 테스트 실행 |

## 파일 구성

```text
day2-fastapi/
├─ main.py          # 앱, API 경로, HTTP 예외 처리
├─ schemas.py       # DocumentRequest, DocumentResponse
├─ processor.py     # 비동기 문서 처리
├─ test_api.py      # 정상·빈 문서·타입 오류 테스트
└─ README.md
```

## 구현한 API

| 메서드 | 경로 | 기능 |
| --- | --- | --- |
| GET | `/hello` | 인사 메시지 반환 |
| POST | `/documents` | 문서 공백 정규화와 문자 수 계산 |

서버는 **HTTP 메서드와 경로**를 함께 보고 실행할 함수를 찾는다.

```python
# 서버: POST /documents 요청을 받을 함수 등록
@app.post("/documents")
async def create_document(document: DocumentRequest):
    ...

# 테스트: POST /documents 요청 전송
response = client.post("/documents", json={...})
```

JSON은 요청 데이터이며, 요청 방식은 `client.post()`가 지정한다.
Swagger UI에서는 해당 API의 Execute 버튼을 누를 때 요청이 전송된다.

## 실행 방법

Git Bash에서 `ai-practice` 폴더를 기준으로 실행한다.

```bash
source venv/Scripts/activate
python -m pip install fastapi uvicorn httpx pytest
cd day2-fastapi
python -m uvicorn main:app --reload
```

- `python -m uvicorn`: 현재 Python 환경의 Uvicorn 실행
- `main:app`: `main.py` 안의 `app` 객체 사용
- `--reload`: 코드 저장 시 서버 자동 재시작
- `Ctrl + C`: 서버 종료

접속 주소:

- 인사 API: http://127.0.0.1:8000/hello
- Swagger UI: http://127.0.0.1:8000/docs

Swagger UI는 API 선언과 Pydantic 스키마를 바탕으로 자동 생성되는 문서·테스트 화면이다.

## 정상 요청과 응답

요청:

```json
{
  "document_id": 1,
  "title": "휴가 규정",
  "content": "연차는   3일 전에\n신청합니다."
}
```

처리 흐름:

```text
POST /documents
→ DocumentRequest로 요청 검증
→ create_document() 실행
→ await process_document(document)
→ 공백 정리 및 문자 수 계산
→ DocumentResponse 생성
→ HTTP 200과 JSON 응답
```

응답:

```json
{
  "document_id": 1,
  "normalized_content": "연차는 3일 전에 신청합니다.",
  "character_count": 16
}
```

현재 코드는 처리 함수에서 `DocumentResponse` 객체를 생성해 반환한다.
라우트에 `response_model=DocumentResponse`를 명시하는 설정은 아직 추가하지 않았다.

## 오류 처리

### 빈 문서: HTTP 400

공백 문자열은 문자열 타입이므로 요청 타입 검증을 통과한다.
이후 `processor.py`에서 내용이 비어 있는지 검사한다.

```python
if not document.content.strip():
    raise ValueError("문서 내용이 비어 있습니다.")
```

`main.py`는 이 예외를 잡아 HTTP 예외로 변환한다.

```python
except ValueError as error:
    raise HTTPException(
        status_code=400,
        detail=str(error),
    ) from error
```

- `str(error)`: ValueError에 넣었던 메시지
- `detail`: FastAPI의 기본 HTTPException 응답에서 사용하는 키
- `from error`: 기존 예외를 새로운 예외의 원인으로 연결하며, 응답 메시지를 추가하는 문법은 아님

응답:

```json
{
  "detail": "문서 내용이 비어 있습니다."
}
```

### 잘못된 ID 타입: HTTP 422

`document_id`에 `"abc"`를 보내면 정수로 변환할 수 없어 요청 검증 단계에서 거부된다.
이때 `create_document()`와 `process_document()`는 실행되지 않는다.

### 실습에서 확인한 상태 코드

| 상태 코드 | 의미 |
| --- | --- |
| 200 | 정상 처리 |
| 400 | 직접 구현한 검사에서 빈 문서를 거부 |
| 404 | 등록되지 않은 경로로 요청: `/document`와 `/documents` 오타 주의 |
| 422 | 필수 필드나 타입 등 요청 스키마 검증 실패 |

## 자동 테스트

```bash
python -m pytest test_api.py -v
```

반드시 `test_api.py`가 있는 `day2-fastapi` 폴더에서 실행한다.

| 테스트 | 확인 내용 |
| --- | --- |
| `test_create_document_success` | HTTP 200과 정규화된 응답 JSON |
| `test_create_document_empty_content` | HTTP 400과 오류 메시지 |
| `test_create_document_invalid_id` | HTTP 422 |

실습 결과: **3개 테스트 통과**.

`TestClient(app)`은 앱에 직접 요청을 전달하므로 Uvicorn을 별도로 실행하지 않아도 된다.
테스트 코드에서는 동기 방식의 `client.post()`를 사용하므로 `async def`나 `@pytest.mark.asyncio`가 필요하지 않다.

## 1일차와 달라진 점

- 1일차: 처리 함수를 직접 호출하고 결과·오류를 터미널에 출력
- 2일차: HTTP 요청으로 처리 함수를 호출하고 결과·오류를 JSON과 상태 코드로 응답
- 함수의 반환값 검사에서 API 상태 코드와 응답 JSON 검사로 테스트 범위를 확장

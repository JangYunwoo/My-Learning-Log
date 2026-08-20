# Day 1 - Python 비동기 처리

## 학습 내용

- `@dataclass`를 사용한 입력·출력 자료형 정의
- `async def`, `await`, `asyncio.run()`을 사용한 비동기 실행
- `asyncio.gather()`를 사용한 여러 작업의 동시 처리
- `raise`와 `try/except`를 사용한 예외 처리
- `pytest`, `pytest-asyncio`를 사용한 비동기 테스트

## 파일 구성

```text
day1-python-async/
├─ main.py
├─ models.py
├─ processor.py
└─ test_processor.py
```

- `models.py`: `Document`, `ProcessResult` 자료형 정의
- `processor.py`: 문서 정규화와 빈 문서 검사
- `main.py`: 정상 처리, 예외 처리, 동시 처리 실행
- `test_processor.py`: 정상 처리와 빈 문서 예외 자동 테스트

## 처리 흐름

```text
Document 입력
→ 빈 내용 검사
→ 비동기 작업 대기
→ 공백과 줄바꿈 정규화
→ 문자 수 계산
→ ProcessResult 반환
```

문서 내용이 비어 있거나 공백만 있으면 다음 예외가 발생한다.

```text
ValueError: 문서 내용이 비어 있습니다.
```

## 실행

저장소의 `ai-practice` 디렉터리에서 가상환경을 활성화한다.

```bash
source venv/Scripts/activate
cd day1-python-async
python main.py
```

실행 시간 확인:

```bash
time python main.py
```

`asyncio.gather()`로 1초짜리 작업 두 개를 동시에 실행하면 두 작업 구간은 약 1초에 완료된다.

## 테스트

필요한 패키지:

```bash
python -m pip install pytest pytest-asyncio
```

테스트 실행:

```bash
python -m pytest test_processor.py -v
```

확인하는 동작:

- 정상 문서가 정규화된 `ProcessResult`를 반환하는가
- 빈 문서가 `ValueError`를 발생시키는가

## 핵심 정리

- `async def` 함수는 호출만 해서는 실행되지 않으며 `await` 또는 `asyncio.run()`이 필요하다.
- `await`로 대기하는 동안 이벤트 루프는 다른 비동기 작업을 실행할 수 있다.
- `asyncio.gather()`는 전달받은 비동기 작업을 함께 실행하고 결과를 순서대로 반환한다.
- `pytest.mark.asyncio`는 pytest가 비동기 테스트를 실행하도록 표시한다.
- `pytest.raises()`는 지정한 예외가 실제로 발생하는지 검사한다.

# API 동작 테스트
from fastapi.testclient import TestClient

from main import app

# FastAPI 앱에 테스트용 HTTP 요청을 보내는 클라이언트
client = TestClient(app)

def test_create_document_success():
    # POST / documents에 JSON 데이터를 보냄
    response = client.post(
        "/documents",
        json={
            "document_id": 1,
            "title": "휴가 규정",
            "content": "연차는     3일  전에 신청합니다.",
        },
    )

    # 정상 처리 상태 코드인지 검사한다.
    assert response.status_code == 200

    # 응답 JSON이 예상 결과와 같은지 검사
    assert response.json() == {
        "document_id": 1,
        "normalized_content": "연차는 3일 전에 신청합니다.",
        "character_count": 16,
    }

def test_create_document_empty_content():

    # 공백만 있는 문서를 요청
    response = client.post(
        "/documents",
        json={
            "document_id": 2,
            "title": "빈 문서",
            "content": "  ",
        },
    )

    # 잘못된 입력에 대해 HTTP 400을 반환하는지 검사.
    assert response.status_code == 400

    # 오류 메시지가 정확한지 검사
    assert response.json() == {
        "detail": "문서 내용이 비어 있습니다."
    }

def test_create_document_invalid_id():

    # 정수여야 하는 document_id에 문자열을 보낸다.
    response = client.post(
        "/documents",
        json={
            "document_id": "abc",
            "title": "휴가 규정",
            "content": "연차는 3일 전에 신청합니다.",
        }
    )

    assert response.status_code == 422

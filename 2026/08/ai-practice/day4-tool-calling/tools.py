# 모델이 사용할 실제 Python 함수

# 실습용 문서 데이터. 문서 ID를 키로 사용
DOCUMENTS = {
    1: "연차는 사용일 3일 전까지 신청해야 합니다.",
    2: "출장비는 영수증 제출 후 지급합니다.",
}

# 문서 ID를 받아 해당 문서의 내용을 반환
def get_document(document_id: int) -> str:
    if document_id not in DOCUMENTS:
        raise ValueError("해당 문서를 찾을 수 없습니다.")

    return DOCUMENTS[document_id]

# 모델에 전달할 도구 설명. 실제 함수를 실행하는 코드는 아니다.
DOCUMENT_TOOL = {
    "type": "function",
    "function": {
        # 호출할 함수 이름
        "name": "get_document",

        # 언제 사용하는 함수인지 설명
        "description": "문서 ID로 문서 내용을 조회합니다.",

        # 함수에 전달할 인자의 구조
        "parameters": {
            "type": "object",

            # 각 인자의 이름과 자료형
            "properties": {
                "document_id": {
                    "type": "integer",
                    "description": "조회할 문서의 ID",
                },
            },

            # 반드시 전달해야 하는 인자
            "required": ["document_id"],
        },
    },
}
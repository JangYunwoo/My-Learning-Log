# FastAPI 앱과 경로 정의
from fastapi import FastAPI, HTTPException
from schemas import DocumentRequest
from processor import process_document

app = FastAPI()

@app.get("/hello")
async def hello():
    return {"message": "안녕하세요"}

# POST /documents 요청을 아래 함수에 연결한다.
@app.post("/documents")
async def create_document(document: DocumentRequest):
    try:
        #문서를 처리하고 결과를 응답
        return await process_document(document)
    except ValueError as error:
        # 처리 과정의 입력 오류를 HTTP 400 응답으로 변환
        raise HTTPException(
            status_code=400,
            detail=str(error),
        ) from error
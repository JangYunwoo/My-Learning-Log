# 모델에 질문과 사용 가능한 도구 정보를 전달하는 코드

from ollama import AsyncClient
from tools import DOCUMENT_TOOL

# 로컬에서 실행중인 Ollama 서버에 연결한다.
client = AsyncClient(host="http://localhost:11434")

async def request_tool(prompt: str):
    response = await client.chat(
        model="qwen3:4b",
        messages=[
            {"role": "user", "content": prompt},
        ],
        # 모델이 선택할 수 있는 도구의 설명을 전달한다.
        tools=[DOCUMENT_TOOL],
        think=True,
        stream=False,
    )

    # 최종 답변뿐 아니라 도구 호출 정보도 확인하도록 메시지를 반환한다.
    return response.message

# 질문, 모델의 도구 호출 요청, 실제 실행 결과를 받아 최종 답변을 요청한다.
async def answer_with_tool_result(
        prompt: str,
        tool_message,
        tool_result: str,
) -> str:
    response = await client.chat(
        model="qwen3:4b",
        messages=[
            # 1. 사용자가 처음 보낸 질문
            {"role": "user", "content": prompt},

            # 2. 모델이 보냈던 도구 호출 요청
            tool_message,

            # 3. Python 함수가 실행한 결과
            {
                "role": "tool",
                "tool_name": "get_document",
                "content": tool_result,
            },
        ],
        think=True,
        stream=False,
    )

    # 도구 실행 결과를 참고해서 모델이 작성한 최종 답변
    return response.message.content
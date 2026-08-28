# Ollama에 질문을 보내고 모델의 최종 답변을 받아 반환

from ollama import AsyncClient
from prompts import SYSTEM_PROMPT, JSON_SYSTEM_PROMPT

# 내 컴퓨터에서 실행중인 Ollama 서버에 연결
client = AsyncClient(host="http://localhost:11434")

# 예제 1: 질문을 모델에 보내고 최종 답변을 반환
async def ask_llm(prompt: str) -> str:
    response = await client.chat(
        model="qwen3:4b",
        messages=[
            # 모델의 역할과 답변 규칙을 전달
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
        ],
        think=True,
        stream=False,
    )

    # 추론용 텍스트가 아닌 최종 답변만 반환
    return response.message.content

# 예제 2: 문서를 요약하고 JSON 형식의 문자열을 반환
async def ask_llm_json(prompt: str) -> str:
    response = await client.chat(
        model="qwen3:4b",
        messages=[
            {"role": "system", "content": JSON_SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
        ],
        format="json", # OLLama에 JSON 형식 출력을 지정
        think=True,
        stream=False,
    )

    # 아직 Python 딕셔너리가 아니라 JSON 문자열임
    return response.message.content
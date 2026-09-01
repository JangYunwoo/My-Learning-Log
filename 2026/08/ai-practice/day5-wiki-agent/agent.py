# 모델 호출 → 도구 실행 → 결과 전달을 반복

from ollama import AsyncClient

from prompts import SYSTEM_PROMPT, WIKI_SYSTEM_PROMPT
from tools import (
    search_documents,
    read_document,
    save_wiki,
    SEARCH_DOCUMENT_TOOL,
    READ_DOCUMENT_TOOL,
    SAVE_WIKI_TOOL,
)

# 로컬에서 실행 중인 Ollama 서버에 연결
client = AsyncClient(host="http://localhost:11434")

# 사용자 요청과 사용 가능한 도구를 모델에 전달
async def request_first_tool(user_request: str):
    response = await client.chat(
        model="qwen3:4b",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_request},
        ],
        tools=[
            SEARCH_DOCUMENT_TOOL,
            READ_DOCUMENT_TOOL,
        ],
        think=True,
        stream=False,
    )

    # 도구 호출 정보를 확인할 수 있도록 전체 메시지를 반환
    return response.message

def execute_tool(tool_call):
    function_name = tool_call.function.name
    arguments = tool_call.function.arguments

    if function_name == "search_documents":
        return search_documents(**arguments)

    if function_name == "read_document":
        return read_document(**arguments)

    if function_name == "save_wiki":
        return save_wiki(**arguments)

    raise ValueError(f"지원하지 않는 도구입니다: {function_name}")

async def request_next_tool(
        user_request: str,
        tool_message,
        tool_result,
):
    response = await client.chat(
        model="qwen3:4b",
        messages=[
            # 사용자의 원래 요청
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_request},

            # 모델이 보낸 첫 번쨰 도구 호출을 요청
            tool_message,

            # Python이 실행한 첫 번째 도구의 결과
            {
                "role": "tool",
                "tool_name": tool_message.tool_calls[0].function.name,
                "content": str(tool_result),
            },
        ],
        tools=[
            SEARCH_DOCUMENT_TOOL,
            READ_DOCUMENT_TOOL,
        ],
        think=True,
        stream=False,
    )

    #모델이 선택한 다음 작업을 확인하기 위해 메시지 전체를 반환
    return response.message

# 검색과 읽기 과정을 모두 전달하고 최종 답변을 요청
async def request_final_answer(
        user_request: str,
        search_message,
        search_result,
        read_message,
        read_result,
) -> str:
    response = await client.chat(
        model="qwen3:4b",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_request},

            # 검색 도구를 요청하고 실행한 기록
            search_message,
            {
                "role": "tool",
                "tool_name": search_message.tool_calls[0].function.name,
                "content": str(search_result),
            },

            # 읽기 도구를 요청하고 실행한 기록
            read_message,
            {
                "role": "tool",
                "tool_name": read_message.tool_calls[0].function.name,
                "content": str(read_result),
            },
        ],
        think=True,
        stream=False,
    )

    return response.message.content

async def request_agent_step(messages: list):
    response = await client.chat(
        model="qwen3:4b",
        messages=messages,
        tools=[
            SEARCH_DOCUMENT_TOOL,
            READ_DOCUMENT_TOOL,
        ],
        think=True,
        stream=False,
    )

    return response.message

# 모델이 도구 사용을 끝내고 답변할 때까지 반복
async def run_agent(user_request: str) -> str:
    # 모델에 계속 전달할 전체 작업 기록
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_request},
    ]

    # 무한 반복을 막기 위해 최대 5단계까지만 실행
    for step in range(5):
        print(f"Agent 단계 {step + 1}")

        # 지금까지의 기록을 보고 다음 행동을 요청
        agent_message = await request_agent_step(messages)

        # 모델이 보낸 메시지도 다음 요청에서 기억할 수 있게 추가
        messages.append(agent_message)

        # 도구 호출이 없으면 모델의 최종 답변으로 보고 종료
        if not agent_message.tool_calls:
            return agent_message.content

        # 모델이 요청한 도구들을 하나씩 실행
        for tool_call in agent_message.tool_calls:
            tool_result = execute_tool(tool_call)

            print("도구:", tool_call.function.name)
            print("결과:", tool_result)

            # 실행 결과를 대화 기록에 추가
            messages.append(
                {
                    "role": "tool",
                    "tool_name": tool_call.function.name,
                    "content": str(tool_result),
                }
            )

    # 5단계 안에 최종 답변이 나오지 않으면 오류를 발생
    raise RuntimeError("Agent가 최대 실행 횟수를 초과했습니다.")

# 위키 작성 기록을 보고 다음 도구 또는 최종 답변을 요청
async def request_wiki_agent_step(messages: list):
    response = await client.chat(
        model="qwen3:4b",
        messages=messages,
        tools=[
            SEARCH_DOCUMENT_TOOL,
            READ_DOCUMENT_TOOL,
            SAVE_WIKI_TOOL,
        ],
        think=True,
        stream=False,
    )

    return response.message

# 모뎅리 위키 저장을 마치고 최종 답변할 때까지 반복
async def run_wiki_agent(user_request: str) -> str:
    messages = [
        {"role": "system", "content": WIKI_SYSTEM_PROMPT},
        {"role": "user", "content": user_request},
    ]

    # 검색, 읽기, 저장, 최종 답변에 필요한 충분한 횟수를 제공
    for step in range(8):
        print(f"WIki Agent 단계 {step + 1}")

        # 지금까지의 기록을 보고 다음 행동을 요청
        agent_message = await request_wiki_agent_step(messages)
        messages.append(agent_message)

        # 도구 요청이 없다면 최종 답변을 반환
        if not agent_message.tool_calls:
            return agent_message.content

        # 모델이 요청한 도구를 하나씩 실행
        for tool_call in agent_message.tool_calls:
            tool_result = execute_tool(tool_call)

            print("도구:", tool_call.function.name)
            print("결과:", tool_result)

            # 실행 결과를 모델이 다음 단계에서 확인할 수 있게 기록
            messages.append(
                {
                    "role": "tool",
                    "tool_name": tool_call.function.name,
                    "content": str(tool_result),
                }
            )

    raise RuntimeError("Wiki Agent가 최대 실행 횟수를 초과했습니다.")
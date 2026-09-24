# 사용자 요청을 준비하고 Agent 실행

import asyncio

from tools import search_documents, read_document, save_wiki
from agent import (
    request_first_tool,
    execute_tool,
    request_next_tool,
    request_final_answer,
    run_agent,
    run_wiki_agent,
)

# 예제 1: 문서 내용에서 "연차"를 검색
search_result1 = search_documents(query="연차")
print("검색 결과:",search_result1)

# 예제 2: 검색된 첫 번째 문서의 내용을 읽음
document_content2 = read_document(file_name=search_result1[0])

print("문서 내용:")
print(document_content2)
print()

# 예제 3: "출장비"가 포함된 문서를 검색
search_result3 = search_documents(query="출장비")
print("출장비 검색 결과:", search_result3)
print()

# 예제 10: 모델 없이 위키 저장 함수를 직접 실행
saved_file10 = save_wiki(
    file_name="leave_guide",
    title="연차 신청 안내",
    content="연차는 사용일 3일 전까지 신청해야 합니다.",
    source_documents=["leave.txt"],
)

print("저장된 위키 파일:", saved_file10)

# 예제 4: "Wiki Agent가 처음 선택한 도구를 확인"
async def main():
    user_request4 = "연차 관련 문서를 찾아서 내용을 알려줘."

    print("Agent의 도구 선택을 기다리는중...")
    message4 = await request_first_tool(user_request4)

    print("첫 번쨰 도구 호출:", message4.tool_calls)

    # 예제 5: 첫 번째 도구 호출 요청을 실제로 실행
    if message4.tool_calls:
        tool_call5 = message4.tool_calls[0]
        tool_result5 = execute_tool(tool_call5)

        print("첫 번쨰 도구 실행 결과:", tool_result5)

        # 예제 6: 검색 결과를 전달하고 다음 도구 선택을 요청
        message6 = await request_next_tool(
            user_request=user_request4,
            tool_message=message4,
            tool_result=tool_result5,
        )

        print("두 번째 도구 호출:", message6.tool_calls)

        # 예제 7: 두 번째 도구 호출 요청을 실제로 실행
        if message6.tool_calls:
            tool_call7 = message6.tool_calls[0]
            tool_result7 = execute_tool(tool_call7)

            print("두 번째 도구 실행 결과:")
            print(tool_result7)

            # 예제 8: 검색, 읽기 결과를 바탕으로 최종 답변을 생성
            final_answer8 = await request_final_answer(
                user_request=user_request4,
                search_message=message4,
                search_result=tool_result5,
                read_message=message6,
                read_result=tool_result7,
            )

            print("최종 답변:")
            print(final_answer8)

            # 예제 9: 모델이 다음 단계를 직접 선택하는 Agent 루프를 실행
            user_requset9 = "출장비 관련 문서를 찾아서 내용을 알려줘."

            print("\nAgent 루프를 시작합니다.")
            final_answer9 = await run_agent(user_requset9)

            print("Agent 최종 답변:")
            print(final_answer9)

            # 예제 11: 검색, 읽기, 저장을 스스로 수행하는 Wiki Agent를 실행
            user_request11 = "연차 관련 문서를 찾아서 위키 파일로 만들어줘."

            print("\nWiki Agent를 시작합니다.")
            final_answer11 = await run_wiki_agent(user_request11)

            print("Wiki Agent 최종 답변:")
            print(final_answer11)

asyncio.run(main())
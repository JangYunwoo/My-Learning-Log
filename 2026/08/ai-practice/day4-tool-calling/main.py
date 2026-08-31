# 질문 준비 → 모델 호출 → 선택된 함수 실행을 연결하는 시작점

import asyncio

from tools import get_document, DOCUMENT_TOOL
from llm_client import request_tool, answer_with_tool_result

# 예제 1: 모델 없이 함수를 직접 호출
document1 = get_document(document_id=1)
print(document1)

# 예제 2: 존재하지 않는 문서를 조회
try:
    document2 = get_document(document_id=999)
    print(document2)
except ValueError as error:
    # get_document()에서 발생시킨 예외를 잡아 출력
    print("문서 조회 실패:", error)

# 예제 3: 모델에 알려줄 함수 이름과 필수 인자를 확인
print("도구 이름:", DOCUMENT_TOOL["function"]["name"])
print("필수 인자:", DOCUMENT_TOOL["function"]["parameters"]["required"])

# 예제 4: 모델이 요청한 도구 호출 정보를 확인
async def main():
    prompt4 = "1번 문서의 내용을 조회해줘."
    prompt6 = "999번 문서의 내용을 조회해줘"

    print("모델의 도구 선택을 기다리는 중...")
    message4 = await request_tool(prompt4)

    '''
    아직 함수를 실행하지 않고 호출 요청만 출력
    print("도구 호출 요청:", message4.tool_calls)
    '''

    # 모델이 도구 호출을 요청했는지 확인
    if message4.tool_calls:
        # 목록에서 첫 번째 호출 요청을 꺼냄
        tool_call4 = message4.tool_calls[0]

        # 요청한 함수 이름과 인자를 각각 저장
        function_name4 = tool_call4.function.name
        arguments4 = tool_call4.function.arguments

        print("함수 이름:", function_name4)
        print("전달할 인자:", arguments4)

        # 우리가 허용한 함수 이름인지 확인
        if function_name4 == "get_document":
            # 모델이 전달한 인자 딕셔너리를 풀어서 함수를 호출
            try:
                # 모델이 요청한 문서를 조회
                tool_result4 = get_document(**arguments4)
            except ValueError as error:
                # 없는 문서라면 오류를 출력하고 main()을 종료
                print("도구 실행 실패:", error)
                return
            
            print("도구 실행 결과:", tool_result4)
            # 실행 결과를 모델에 돌려주고 최종 답변을 받는다.
            prompt5 = "문서 번호를 언급하고 이를 바탕으로 신청 기한을 판단해줘"
            answer4 = await answer_with_tool_result(
                prompt=prompt5,
                tool_message=message4,
                tool_result=tool_result4,
            )
            print("최종 답변:", answer4)
        else:
            print("지원하지 않는 도구입니다:", function_name4)
    else:
        print("모델이 도구 호출을 요청하지 않았습니다.")

asyncio.run(main())
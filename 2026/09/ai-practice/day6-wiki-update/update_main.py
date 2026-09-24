# 기존 위키의 내용을 수정하는 Agent 실행 파일

import asyncio

from agent import run_wiki_update_agent

async def main():
    # 예제 1: 기존 위키에 원본문서의 내용을 추가하도록 요청
    update_request1 = (
        "leave_guide.md 위키를 수정해줘."
        "원본문서를 확인해서 부서장 승인 조건과 "
        "긴급한 경우의 처리 방벙을 추가해줘."
    )

    print("Wiki Update Agent를 시작합니다.")
    final_answer1 = await run_wiki_update_agent(update_request1)

    print("Wiki Update Agent 최종 답변:")
    print(final_answer1)

asyncio.run(main())
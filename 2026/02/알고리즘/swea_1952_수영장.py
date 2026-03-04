def dfs(month, fee):
    global answer
    # 누적 요금이 저장해놓은 값 보다 초과했을 때
    if fee >= answer:
        return
     
    # 모든 월에 대해 지불했을 때
    if month >= 12:
        if fee < answer:
            answer = fee
        return
     
    # 일권
    dfs(month+1, fee+(day_fee*days[month]))
    # 월권
    dfs(month+1, fee+month_fee)
    # 3개월권
    dfs(month+3, fee+quarter_fee)
 
T = int(input())
 
for tc in range(1, T+1):
    day_fee, month_fee, quarter_fee, answer = map(int, input().split()) # 10 40 100 300
    days = list(map(int, input().split())) # 0 0 2 9 1 5 0 0 0 0 0 0
     
    dfs(0, 0)
     
    print(f'#{tc} {answer}')

    # 모두 일권으로 사는방법 ~ 보두 3개월권으로 사는 방법을 찾아서 1년권 answer와 비교하여
    # 이보다 크면 버리고 이보다 작으면 최소값 갱신 시행
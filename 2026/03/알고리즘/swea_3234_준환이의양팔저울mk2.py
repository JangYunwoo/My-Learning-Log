def dfs(count, visited, left, right):
    if count == N:
        return 1
    
    temp = 0
    for i in range(N):
        # i번째 무게추를 골랐다면 건너뛰기
        if visited & (1 << i):
            continue
        
        # 현재 방문 상태에서 
        if dp[visited].get(left):
            return dp[visited][left]
        
        temp += dfs(count+1, visited | (1 << i), left+weights[i], right)
        if left >= right+weights[i]:
            temp += dfs(count+1, visited | (1 << i), left, right+weights[i])
    
    # 현재 visited 상태에서 left 무게일 때의 경우의 수를 반환
    dp[visited][left] = temp
    return dp[visited][left]

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    weights = list(map(int, input().split()))

    dp = [{} for _ in range(2**N)]
    print(f"#{tc} {dfs(0, 0, 0, 0)}")
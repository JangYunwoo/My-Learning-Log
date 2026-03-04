def search(count, sum):
    global result
    
    if sum >= result:
        return
    
    if count == N:
        if sum < result:
            result = sum
        return

    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            search(count+1, sum + board[count][i])
            visited[i] = 0
    return

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [0]*N
    result = float('inf')

    search(0, 0)

    print(f"#{tc} {result}")
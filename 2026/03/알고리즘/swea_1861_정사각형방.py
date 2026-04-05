from collections import deque

def bfs(a, b):
    q = deque()
    q.append([a, b])
    count = 1
    while q:
        x, y = q.popleft()
        for dir in range(4):
            nx = x+dr[dir]
            ny = y+dc[dir]
            if 0<=nx<N and 0<=ny<N and board[nx][ny] == board[x][y]+1:
                visited[nx][ny] = 1
                q.append([nx, ny])
                count += 1

    return count

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    result = 0
    result_num = float('inf')

    for r in range(N):
        for c in range(N):
            if visited[r][c] == 0:
                test = bfs(r, c)
                if test > result:
                    result_num = board[r][c]
                    result = test
                elif test == result:
                    if board[r][c] < result_num:
                        result_num = board[r][c]
                visited[r][c] = 1
    
    print(f"#{tc} {result_num} {result}")
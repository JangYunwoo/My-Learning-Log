from collections import deque
 
dr = [0,1,0,-1]
dc = [1,0,-1,0]
 
T= int(input())
 
for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int, input())) for _ in range(N)]
 
    visited = [[-1]*N for _ in range(N)]
    q = deque()
    q.append([0, 0])
    visited[0][0] = 0
    while q:
        x, y = q.popleft()
        for dir in range(4):
            nx = x+dr[dir]
            ny = y+dc[dir]
            if 0<=nx<N and 0<=ny<N:
                if visited[nx][ny] == -1 or visited[x][y] + board[nx][ny]  < visited[nx][ny]:
                    visited[nx][ny] = visited[x][y] + board[nx][ny]
                    q.append([nx, ny])
 
    result = visited[-1][-1]
 
    print(f"#{tc} {result}")
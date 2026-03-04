from collections import deque
 
dr = [-1,1,0,0]
dc = [0,0,-1,1]
 
for _ in range(10):
    tc = int(input())
    board = [list(map(int, input())) for _ in range(16)]
    visited = [[0]*16 for _ in range(16)]
 
    q = deque()
    for r in range(16):
        for c in range(16):
            if board[r][c] == 2:
                q.append([r, c])
                visited[r][c] = 1
        if q:
            break
 
    while q:
        x, y = q.popleft()
        if board[x][y] == 3:
            result = 1
            break
        for dir in range(4):
            nx = x+dr[dir]
            ny = y+dc[dir]
            if 0<=nx<16 and 0<=ny<16 and visited[nx][ny] == 0 and board[nx][ny] != 1:
                q.append([nx, ny])
                visited[nx][ny] = 1
    else:
        result = 0
 
    print(f"#{tc} {result}")
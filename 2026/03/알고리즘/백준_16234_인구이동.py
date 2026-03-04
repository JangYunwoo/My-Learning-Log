from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

N, L, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

q = deque()
avercunt = deque()
day = 0
while True:
    switch = 0
    visited = [[0]*N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if visited[r][c] == 0:
                for dir in range(4):
                    nr = r+dr[dir]
                    nc = c+dc[dir]
                    if 0<=nr<N and 0<=nc<N and visited[nr][nc] == 0:
                        if L<=(abs(board[r][c] - board[nr][nc]))<=R:
                            switch = 1
                            q = deque()
                            avercunt = deque()
                            q.append([r, c])
                            avercunt.append([r, c])
                            sumpop = board[r][c]
                            visited[r][c] = 1
                            break
                while q:
                    x, y = q.popleft()
                    for dir2 in range(4):
                        nx = x+dr[dir2]
                        ny = y+dc[dir2]
                        if 0<=nx<N and 0<=ny<N and visited[nx][ny] == 0:
                            if L<=(abs(board[x][y] - board[nx][ny]))<=R:
                                q.append([nx, ny])
                                avercunt.append([nx, ny])
                                sumpop += board[nx][ny]
                                visited[nx][ny] = 1
                if avercunt:
                    averpop = sumpop // len(avercunt)
                    while avercunt:
                        a, b = avercunt.popleft()
                        board[a][b] = averpop
    
    if switch:
        day += 1
    else:
        print(day)
        break
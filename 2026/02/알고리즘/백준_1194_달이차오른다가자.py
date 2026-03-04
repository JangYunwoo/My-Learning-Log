from collections import deque

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

dr = [-1,1,0,0]
dc = [0,0,-1,1]
visited = [[{} for _ in range(M)] for _ in range(N)]
q = deque()
for r in range(N):
    for c in range(M):
        if board[r][c] == '0':
            q.append([r, c, '000000'])
            board[r][c] = '.'
            visited[r][c]['000000'] = 1
    if q:
        break

count = 0
while q:
    count += 1
    for _ in range(len(q)):
        x, y, k = q.popleft()
        for dir in range(4):
            nx = x+dr[dir]
            ny = y+dc[dir]
            if 0<=nx<N and 0<=ny<M and visited[nx][ny].get(k) == None:
                if board[nx][ny] != '#':
                    if board[nx][ny] == '1':
                        print(count)
                        exit()
                    if board[nx][ny].islower():
                        nk = k[:ord(board[nx][ny])-97] + '1' + k[ord(board[nx][ny])-96:]
                    else:
                        nk = k
                    if board[nx][ny].isupper():
                        if nk[ord(board[nx][ny])-65] == '0':
                            continue
                    visited[nx][ny][nk] = 1
                    q.append([nx, ny, nk])
else:
    print(-1)
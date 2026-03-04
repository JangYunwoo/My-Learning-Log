from collections import deque

N, M = map(int, input().split())
sea = [list(map(int, input().split())) for _ in range(N)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

after_year = 0
while True:
    melt = []
    after_year += 1
    for r in range(N):
        for c in range(M):
            if sea[r][c]:
                melt_point = 0
                for dir in range(4):
                    nr = r+dr[dir]
                    nc = c+dc[dir]
                    if 0<=nr<N and 0<=nc<M and not sea[nr][nc]:
                        melt_point += 1
                melt.append([r, c, melt_point])
    
    for _ in range(len(melt)):
        x, y, m = melt.pop()
        sea[x][y] -= m
        if sea[x][y] < 0:
            sea[x][y] = 0
        
    visited = [[0]*M for _ in range(N)]
    count = 0
    for r in range(N):
        for c in range(M):
            if sea[r][c] and not visited[r][c]:
                q = deque([[r, c]])
                visited[r][c] = 1
                count += 1
                while q:
                    for _ in range(len(q)):
                        a, b = q.popleft()
                        for dir in range(4):
                            na = a+dr[dir]
                            nb = b+dc[dir]
                            if 0<=na<N and 0<=nb<M and not visited[na][nb] and sea[na][nb]:
                                q.append([na, nb])
                                visited[na][nb] = 1

    if count > 1:
        break
    
    if count == 0:
        after_year = 0
        break

print(after_year)